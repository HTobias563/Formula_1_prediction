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
    def driver_positions_year(self, year, forename, surname):
            # Filtere den Fahrer anhand des Vornamens und Nachnamens
            driver_data = self.drivers[(self.drivers['forename'] == forename) & (self.drivers['surname'] == surname)]
            if driver_data.empty:
                raise ValueError("Der Fahrer wurde nicht gefunden oder ist in dem Jahr nicht gestartet")
            driver_id = driver_data.iloc[0]['driverId']
            
            # Filtere die Rennen des gewünschten Jahres
            races_in_year = self.races[self.races['year'] == year]
            race_ids = races_in_year['raceId']
            
            # Filtere die Ergebnisse: nur Rennen des Jahres und des gesuchten Fahrers
            positions = self.results[(self.results['raceId'].isin(race_ids)) & (self.results['driverId'] == driver_id)]
            positions = positions.sort_values(by='position')
            
            # Erstelle ein Balkendiagramm der Positionen mit Plotly Express
            fig = px.bar(positions, x="position", title=f"The Race results of {forename} {surname} in {year}")
            return fig

if __name__ == "__main__":
    plotter = PlotGenerator()
    # Beispiel: Race Wins Plot anzeigen
    fig1 = plotter.race_wins_plot('Bahrain Grand Prix', 2023)
    fig1.show()
        
    # Beispiel: Driver Positions Plot anzeigen
    fig2 = plotter.driver_positions_year(2022, "Max", "Verstappen")
    fig2.show()