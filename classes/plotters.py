import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
pio.templates.default = "simple_white"


class Plotter:
    def __init__(self, df, var='energy'):
        self.df = df
        self.var = var

    def make_data_plot(self, html=False):
        fig = make_subplots(specs=[[{'secondary_y': True}]])
        occup = px.line(self.df, y='occupancy')
        occup.update_traces(line_color='#4d5154')
        energy = px.line(self.df, y='kWh')
        energy.update_traces(line_color='#eb6a23')
        fig.add_trace(occup.data[0], secondary_y=True)
        fig.add_trace(energy.data[0])
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),)
        if html:
            html_fig = pio.to_html(fig, full_html=False, default_height=400)
            return html_fig
        else:
            return fig

    def make_result_plot(self, res_df, html=False):
        fig = go.Figure()
        # occup = px.line(self.df, y='occupancy')
        # occup.update_traces(line_color='#4d5154')
        energy = px.line(res_df, y=f'Energy forecast')
        input_energy = px.line(self.df, y=f'consumptionKWh')
        energy.update_traces(line_color='#eb6a23', line=dict(dash='dash'))
        input_energy.update_traces(line_color='#eb6a23')
        # fig.add_trace(occup.data[0], secondary_y=True)
        fig.add_trace(input_energy.data[0])
        fig.add_trace(energy.data[0])
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),)
        if html:
            html_fig = pio.to_html(fig, full_html=False, default_height=400)
            return html_fig
        else:
            return fig


class EnergyPlotter(Plotter):
    def __init__(self, df, var='kWh'):
        super(EnergyPlotter, self).__init__(df, var=var)

    def make_data_plot(self, html=False):
        fig = make_subplots(specs=[[{'secondary_y': True}]])
        occup = px.bar(self.df, y='occupancy')
        occup.update_traces(line_color='#4d5154')
        energy = px.line(self.df, y='kWh')
        energy.update_traces(line_color='#eb6a23')
        fig.add_trace(occup.data[0], secondary_y=True)
        fig.add_trace(energy.data[0])
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),)
        if html:
            html_fig = pio.to_html(fig, full_html=False, default_height=400)
            return html_fig
        else:
            return fig

    def make_result_plot(self, res_df, html=False):
        fig = go.Figure()
        energy = px.line(res_df, y=f'Energy forecast')
        input_energy = px.line(self.df, y=f'{self.var}')
        energy.update_traces(line_color='#eb6a23', line=dict(dash='dash'))
        input_energy.update_traces(line_color='#eb6a23')
        # fig.add_trace(occup.data[0], secondary_y=True)
        fig.add_trace(input_energy.data[0])
        fig.add_trace(energy.data[0])
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),)
        if html:
            html_fig = pio.to_html(fig, full_html=False, default_height=400)
            return html_fig
        else:
            return fig


class OccupancyPlotter(Plotter):
    def __init__(self, df, var='occupancy'):
        super(OccupancyPlotter, self).__init__(df, var=var)

    def make_data_plot(self):
        fig = make_subplots(specs=[[{'secondary_y': True}]])
        occup = px.bar(self.df, y='occupancy')
        occup.update_traces(marker_color='#4d5154')
        energy = px.line(self.df, y='kWh', markers=True)
        energy.update_traces(line_color='#eb6a23')
        fig.add_trace(occup.data[0])
        fig.add_trace(energy.data[0], secondary_y=True)
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),)
        html_fig = pio.to_html(fig, full_html=False, default_height=400)
        return html_fig

    def make_result_plot(self, res_df, html=False):
        fig = go.Figure()
        occupancy = px.bar(res_df, y=f'Occupancy forecast', opacity=0.7)
        input_occupancy = px.bar(self.df, y=f'occupancy')
        occupancy.update_traces(marker_color='#eb6a23')
        input_occupancy.update_traces(marker_color='#4d5154')
        # fig.add_trace(occup.data[0], secondary_y=True)
        fig.add_trace(input_occupancy.data[0])
        fig.add_trace(occupancy.data[0])
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), )
        if html:
            html_fig = pio.to_html(fig, full_html=False, default_height=400)
            return html_fig
        else:
            return fig


class DataPlotter:
    def __init__(self, df, vars=('kWh')):
        self.df = df
        self.vars = vars

    def make_data_plot(self):
        # fig = make_subplots(specs=[[{'secondary_y': True}]])
        fig = px.line(self.df, y=self.vars)
        # occup.update_traces(line_color='#4d5154')
        # energy = px.line(self.df, y='kWh')
        # energy.update_traces(line_color='#eb6a23')
        # fig.add_trace(occup.data[0], secondary_y=True)
        # fig.add_trace(energy.data[0])
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),)
        html_fig = pio.to_html(fig, full_html=False, default_height=400)
        return html_fig

    def make_result_plot(self, res_df, html=False):
        fig = go.Figure()
        # occup = px.line(self.df, y='occupancy')
        # occup.update_traces(line_color='#4d5154')
        energy = px.line(res_df, y=f'Energy forecast')
        input_energy = px.line(self.df, y=f'consumptionKWh')
        energy.update_traces(line_color='#eb6a23', line=dict(dash='dash'))
        input_energy.update_traces(line_color='#eb6a23')
        # fig.add_trace(occup.data[0], secondary_y=True)
        fig.add_trace(input_energy.data[0])
        fig.add_trace(energy.data[0])
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),)
        if html:
            html_fig = pio.to_html(fig, full_html=False, default_height=400)
            return html_fig
        else:
            return fig

class DataFrameHandler:
    def __init__(self, df, target, date=None):
        self.df = df
        self.target = target
        self.date = self.get_date(date)
        self.steps = self.get_steps()
        self.df_f = self.filter_df()

    def get_date(self, date):
        if date is None:
            date = self.df.index[-1]
        elif date is '':
            date = self.df.index[-1]
        else:
            date = pd.to_datetime(date, dayfirst=True)
        return date

    def get_steps(self):
        hours_dict = {'day': 168, 'week': 168, 'month': 720}
        steps = hours_dict[self.target]
        return steps

    def filter_df(self):
        print(self.date, self.steps)
        input_df = self.df.loc[pd.to_datetime(self.date) - pd.to_timedelta(f'{self.steps}h'): self.date]
        return input_df


if __name__ == '__main__':
    pass