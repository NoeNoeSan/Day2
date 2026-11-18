import gradio as gr

def calculate(a,b):
    return a+b

demo = gr.Interface(
    fn = calculate,
    inputs = [
        gr.Number(label = "First Number"),
        gr.Number(label="Second Number"),
    ],
    outputs = gr.Number(label="Total"),
    title= "Calculator"
)
demo.launch()