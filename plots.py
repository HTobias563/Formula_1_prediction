# plots.py
import plotly.graph_objects as go

class PlotGenerator:
    def create_plot(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 9]))
        fig.update_layout(title="Formel 1 Performance")
        return fig
