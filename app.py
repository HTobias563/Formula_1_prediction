import gradio as gr
from plots import PlotGenerator

plotter = PlotGenerator()

def show_plot():
    return plotter.create_plot()

with gr.Blocks() as demo:
    gr.HTML("""
        <div style="display: flex; flex-direction: column; align-items: center; font-family: 'Courier New', sans-serif;">
            <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmXwvdFYsHObbXaxFauMwKO-k3MjcWVzx5kT4jMh3eOlV9hFhsijdinE93sX9dCSGvCKw&usqp=CAU' 
                 alt='Formel 1 Logo' style='width:200px; margin-bottom: 10px;'/>
            <h1 style="color: #FF1801; font-family: 'Orbitron', sans-serif; font-size: 64 px; margin: 0;"> Formel 1 Dashboard</h1>
            <p style="font-size: 18px; margin-top: 5px;">Hier findest du aktuelle Daten zur Saison 2025.</p>
        </div>
    """)



    with gr.Row():
        plot_output = gr.Plot(label="Interaktiver Formel 1 Plot")
        plot_button = gr.Button("Zeige Plot")

    plot_button.click(fn=show_plot, inputs=[], outputs=plot_output)

demo.launch()
