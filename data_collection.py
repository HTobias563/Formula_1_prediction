import requests
import pandas as pd

def get_race_results(year):
    # Definiere die API-URL mit dem angegebenen Jahr und setze ein hohes Limit, um alle Ergebnisse zu erhalten
    url = f"http://ergast.com/api/f1/{year}/results.json?limit=100000"
    response = requests.get(url)
    data = response.json()

    race_data = []
    
    # Iteriere über alle Rennen des Jahres
    for race in data["MRData"]["RaceTable"]["Races"]:
        gp_name = race["raceName"]
        circuit = race["Circuit"]["circuitName"]
        
        # Iteriere über alle Ergebnisse eines Rennens
        for result in race["Results"]:
            driver = result["Driver"]["familyName"]
            team = result["Constructor"]["name"]
            start_pos = result["grid"]
            finish_pos = result["position"]
            
            # Füge die gesammelten Daten der Liste hinzu
            race_data.append([year, gp_name, circuit, driver, team, start_pos, finish_pos])

    # Erstelle einen DataFrame mit den gesammelten Daten
    df = pd.DataFrame(race_data, columns=["Jahr", "GP", "Strecke", "Fahrer", "Team", "Startplatz", "Finish"])
    return df

# Abrufen der Daten für 2023
df_race = get_race_results(2023)

# Speichern der Daten in einer CSV-Datei
df_race.to_csv("rennergebnisse.csv", index=False)
print(f"Rennergebnisse für 2023 gespeichert! Gesamtanzahl der Einträge: {len(df_race)}")
