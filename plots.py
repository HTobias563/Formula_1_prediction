import pandas as pd 
import plotly.express as px

class PlotGenerator:
    def __init__(self):
        self.results = pd.read_csv('/Users/hannahtobias/Desktop/Programming/Formula_1_prediction/Formula_1_prediction/f1db_csv/results.csv')
        self.drivers = pd.read_csv('/Users/hannahtobias/Desktop/Programming/Formula_1_prediction/Formula_1_prediction/f1db_csv/drivers.csv')
        self.races = pd.read_csv('/Users/hannahtobias/Desktop/Programming/Formula_1_prediction/Formula_1_prediction/f1db_csv/races.csv')
        self.jahre = sorted(self.races["year"].unique(),reverse=True)
        self.gps = sorted(self.races["name"].unique())

    def race_wins_plot(self, gp_name, year):
        race_row = self.races[
            (self.races['name'].str.contains(gp_name, case=False)) &
            (self.races['year'] == year)
        ]

        if race_row.empty:
            raise ValueError("Rennen nicht gefunden")
        
        race_id = race_row.iloc[0]['raceId']
        results = self.results[self.results['raceId'] == race_id]
        results_with_drivers = results.merge(self.drivers, on="driverId")
        sorted_results = results_with_drivers.sort_values("positionOrder")
        sorted_results["full_name"] = sorted_results["forename"] + " " + sorted_results["surname"]
      
        # Erzeuge den Plotly-Balkendiagramm
        fig = px.bar(sorted_results, x='full_name', y='time', title=f"Race results {gp_name}, {year}")
        return fig

if __name__ == "__main__":
    plotter = PlotGenerator()
    fig = plotter.race_wins_plot('Bahrain Grand Prix', 2023)
    fig.show()
