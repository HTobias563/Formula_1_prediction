import streamlit as st
from datetime import datetime as date
import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plots import PlotGenerator

# Initialisiere den PlotGenerator
plotter = PlotGenerator()


st.title("Mein Formula 1 Dashboard")
st.subheader("Everything you need to know")
st.subheader("")

#countdown 
df = pd.read_csv("/Users/hannahtobias/Desktop/Programming/Formula_1_prediction/Formula_1_prediction/f1db_csv/f1_rennen_2025.csv")
df["Startzeit"] = pd.to_datetime(df["Startzeit"])

now = date.now()
next_race = df[df["Startzeit"] > now].sort_values("Startzeit").iloc[0]
startzeit = next_race["Startzeit"]
session = next_race["Session"]


# Countdown berechnen
countdown = startzeit - now
days = countdown.days
hours, remainder = divmod(countdown.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Ausgabe im schönen Format
st.markdown(f"""
<style>
.countdown-box {{
    background-color: #1e1e1e;
    border-radius: 20px;
    padding: 30px;
    color: white;
    font-size: 36px;
    font-weight: 600;
    text-align: center;
    box-shadow: 0 0 20px rgba(2,0,0,0.4);
}}
</style>

<div class="countdown-box">
    Countdown next Event:<br>
     <span style='font-size: 48px; color: #7096D1;'>{days}d {hours}h {minutes}m {seconds}s</span><br>
    {next_race['Grand Prix']} – {next_race['Ort']}<br>
    {next_race['Session']}


</div>
""", unsafe_allow_html=True)