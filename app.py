import gradio as gr
from plots import PlotGenerator

plotter = PlotGenerator()

# Callback für Race Results (wie bisher)
def show_race_wins(year, gp):
    fig = plotter.race_wins_plot(gp, year)
    return fig

# Callback für Driver Standings
def show_driver_positions(year, driver_name):
    # Erwartet, dass der Name als "Vorname Nachname" eingegeben wird
    try:
        forename, surname = driver_name.split(" ", 1)
    except ValueError:
        return "Bitte gib Vor- und Nachname getrennt durch ein Leerzeichen ein (z.B. 'Max Verstappen')."
    fig = plotter.driver_positions_year(year, forename, surname)
    return fig

with gr.Blocks() as demo:
    gr.HTML("""
        <div style="text-align: center; font-family: 'Courier New', sans-serif;">
            <h1 style="color: #FF1801; font-family: 'Orbitron', sans-serif; font-size: 128px; margin: 0;">Formel 1 Dashboard</h1>
            <p style="font-size: 18px; margin-top: 5px;">Hier findest du aktuelle Daten und einen Überblick der Historischen Daten .</p>
        </div>
    """)


    # Abschnitt für Race Results
    gr.Markdown("### Race Results")
    with gr.Row():
        race_year_dropdown = gr.Dropdown(choices=plotter.jahre, label="Jahr", value=plotter.jahre[0])
        gp_dropdown = gr.Dropdown(choices=plotter.gps, label="GP", value=plotter.gps[0])
    race_button = gr.Button("Generate Race Results ")
    race_output = gr.Plot()
    race_button.click(fn=show_race_wins, inputs=[race_year_dropdown, gp_dropdown], outputs=race_output)

    # Abschnitt für Driver Standings
    gr.Markdown("### Driver Standings")
    with gr.Row():
        driver_year_dropdown = gr.Dropdown(choices=plotter.jahre, label="Jahr", value=plotter.jahre[0])
        driver_name_input = gr.Textbox(label="Fahrername (Vorname Nachname)", placeholder="z.B. Max Verstappen")
    driver_button = gr.Button("Generate Driver Standings ")
    driver_output = gr.Plot()
    driver_button.click(fn=show_driver_positions, inputs=[driver_year_dropdown, driver_name_input], outputs=driver_output)

demo.launch()
