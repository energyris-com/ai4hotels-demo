import pandas as pd
from classes.forecasters import EnergyForecast, OccupancyForecast
from classes.plotters import DataFrameHandler, EnergyPlotter, OccupancyPlotter



class Hotel:
    def __init__(self, pk, name, file_path, stars, latitude, longitude, countries_list, max_rooms, max_capacity):
        self.pk = pk
        self.init_df = pd.read_csv(file_path, index_col=0, parse_dates=True)
        self.name = name
        self.stars = stars
        self.latitude = latitude
        self.longitude = longitude
        self.countries = countries_list
        self.max_rooms = max_rooms
        self.max_capacity = max_capacity
        self.hourly_df = pd.read_csv('../data/dataframe_energy.csv', index_col=0, parse_dates=True)  # hardcoded for demo
        self.daily_df = pd.read_csv('../data/dataframe_occupancy.csv', index_col=0, parse_dates=True)  # hardcoded for demo

    def get_energy_forecast(self, horizon='week', date='2021-08-10'):
        ef = EnergyForecast(self.hourly_df, f'{horizon}', f'{date}')
        prediction = ef.get_forecast()
        res_df = ef.make_results_df(prediction)
        return res_df

    def plot_energy_forecast(self, res_df, horizon='week', date='2021-08-10'):
        dfh = DataFrameHandler(self.init_df, f'{horizon}', f'{date}')
        ep = EnergyPlotter(dfh.df_f, 'kWh')
        fig = ep.make_result_plot(res_df)
        return fig

    def get_occupancy_forecast(self, horizon='week', date='2021-08-10'):
        of = OccupancyForecast(self.daily_df, f'{horizon}', f'{date}')
        prediction = of.get_forecast()
        res_df = of.make_results_df(prediction)
        return res_df

    def plot_occupancy_forecast(self, res_df, horizon='week', date='2021-08-10'):
        dfh = DataFrameHandler(self.daily_df, f'{horizon}', f'{date}')
        op = OccupancyPlotter(dfh.df_f, 'kWh')
        fig = op.make_result_plot(res_df)
        return fig


