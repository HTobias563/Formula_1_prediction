import gradio as gr
from plots import PlotGenerator

plotter = PlotGenerator()

def show_plot():
    return plotter.create_plot()

# Interface definieren
demo = gr.Interface(fn=show_plot, inputs=[], outputs=gr.Plot(label="Interaktiver Formel 1 Plot"))

demo.launch()
