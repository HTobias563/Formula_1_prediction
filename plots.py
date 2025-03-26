# plots.py
import plotly.graph_objects as go
import pandas as pd 


class PlotGenerator:
    def __init__(self):
        self.result = pd.read_csv('f1db_csv/results.csv')
        self.drivers = pd.read_csv('f1db_csv/drivers.csv')
        self.races = pd.read_csv('f1db_csv/races.csv')


    def plot_winner(self):
        pass




    def create_plot(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 9]))
        fig.update_layout(title="Formel 1 Performance")
        return fig
