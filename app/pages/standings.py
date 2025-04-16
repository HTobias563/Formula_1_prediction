import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plots import PlotGenerator

# Initialisiere den PlotGenerator
plotter = PlotGenerator()


st.title("Driver and Construction Standings")
st.subheader("learn more ")


# === Abschnitt: Race Results ===
st.subheader("Race Results")
col1, col2 = st.columns(2)
race_year = col1.selectbox("Jahr", options=plotter.jahre, index=0)
gp_choice = col2.selectbox("GP", options=plotter.gps, index=0)

if st.button("Generate Race Results"):
    try:
        fig_race = plotter.race_wins_plot(gp_choice, race_year)
        st.plotly_chart(fig_race, use_container_width=True)
    except Exception as e:
        st.error(f"Fehler bei Race Results: {e}")

st.write("---")

# === Abschnitt: Driver Standings ===
st.subheader("Driver Standings")
col3, col4 = st.columns(2)
driver_year = col3.selectbox("Jahr (Driver Standings)", options=plotter.jahre, index=0)
driver_name = col4.text_input("Fahrername (Vorname Nachname)", value="Max Verstappen")

if st.button("Generate Driver Standings"):
    try:
        forename, surname = driver_name.split(" ", 1)
        fig_driver = plotter.driver_positions_year(driver_year, forename, surname)
        st.plotly_chart(fig_driver, use_container_width=True)
    except ValueError:
        st.error("Bitte gib Vor- und Nachname getrennt durch ein Leerzeichen ein (z.B. 'Max Verstappen').")
    except Exception as e:
        st.error(f"Fehler bei Driver Standings: {e}")
