from keras.models import load_model
import pandas as pd
from keras_self_attention import SeqSelfAttention
from classes.aux_functions import make_one_input
import datetime
import pickle


class EnergyForecast:
    def __init__(self, df, target, date=None):
        self.df = df
        self.target = target
        self.date = self.get_date(date)
        self.steps = self.get_steps()
        self.model_path = f'../models/energy/{target}/maxp_lstm.h5'  # change model name
        self.input_df = self.prepare_df()
        self.n_future = 24 if self.target == 'day' else self.steps

    @staticmethod
    def get_date(date):
        if date is not None:
            date = date
        else:
            date = datetime.date.today()
        return date

    def get_steps(self):
        hours_dict = {'day': 168, 'week': 168, 'month': 720}
        steps = hours_dict[self.target]
        return steps

    def prepare_df(self):
        self.df.index = pd.to_datetime(self.df.index, utc=True, dayfirst=True).tz_localize(None)
        input_df = self.df.loc[pd.to_datetime(self.date) - pd.to_timedelta(f'{self.steps}h'): self.date]
        return input_df

    def get_forecast(self):
        model = load_model(self.model_path, custom_objects={'SeqSelfAttention': SeqSelfAttention})
        sc = pickle.load(open('../scalers/energy_scaler.pkl', 'rb'))
        sc.partial_fit(self.input_df.values)
        df = sc.transform(self.input_df)
        inputs = make_one_input(df, self.steps)
        prediction = model.predict(inputs)
        inv_sc = pickle.load(open('../scalers/inverse_energy_scaler.pkl', 'rb'))
        prediction = inv_sc.inverse_transform(prediction)
        return prediction

    def make_results_df(self, prediction):
        idx = pd.date_range(pd.to_datetime(self.date, dayfirst=True) + pd.to_timedelta(f'1h'),
                            pd.to_datetime(self.date, dayfirst=True) + pd.to_timedelta(f'{self.n_future}h'),
                            freq='h')
        res_df = pd.DataFrame(prediction[0, :], index=idx, columns=['Energy forecast'])
        return res_df

    def predict_and_get_results(self):
        prediction = self.get_forecast()
        res_df = self.make_results_df(prediction)
        return res_df


class OccupancyForecast:
    def __init__(self, df, target, date=None):
        self.df = df
        self.target = target
        self.date = self.get_date(date)
        self.steps = self.get_steps()
        self.model_path = f'../models/occupancy/{target}/cnn_max_lstm_att.h5'  # change model name
        self.input_df = self.prepare_df()

    @staticmethod
    def get_date(date):
        if date is not None:
            date = date
        else:
            date = datetime.date.today()
        return date

    def get_steps(self):
        hours_dict = {'week': 15, 'month': 30}
        steps = hours_dict[self.target]
        return steps

    def prepare_df(self):
        self.df.index = pd.to_datetime(self.df.index, utc=True).date
        input_df = self.df.loc[pd.to_datetime(self.date) - pd.to_timedelta(f'{self.steps}d'): pd.to_datetime(self.date)]
        return input_df

    def get_forecast(self):
        model = load_model(self.model_path, custom_objects={'SeqSelfAttention': SeqSelfAttention})
        sc = pickle.load(open('../scalers/occupancy_scaler.pkl', 'rb'))
        sc.partial_fit(self.input_df.values)
        df = sc.transform(self.input_df)
        inputs = make_one_input(df, self.steps)
        prediction = model.predict(inputs)
        inv_sc = pickle.load(open('../scalers/inverse_occupancy_scaler.pkl', 'rb'))
        prediction = inv_sc.inverse_transform(prediction)
        return prediction

    def make_results_df(self, prediction):
        idx = pd.date_range(pd.to_datetime(self.date, dayfirst=True) + pd.to_timedelta(f'1d'),
                            pd.to_datetime(self.date, dayfirst=True) + pd.to_timedelta(f'{self.steps}d'),
                            freq='d')
        res_df = pd.DataFrame(prediction[0, :], index=idx, columns=['Occupancy forecast'])
        return res_df

    def predict_and_get_results(self):
        prediction = self.get_forecast()
        res_df = self.make_results_df(prediction)
        return res_df