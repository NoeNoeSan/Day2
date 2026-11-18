import gradio as gr

def display(name,study_hours,attendance):
    return f"Student Name: {name} Study_hours: {study_hours} and Attendance: {attendance}"

demo = gr.Interface(
    fn = display,
    inputs = [gr.Textbox(label = "Enter your name :"),
              gr.Number(label = "Enter your study_hours :"),
              gr.Number(label = "Enter your attendance")
              ],
    outputs = gr.Textbox(label = "Student Info"),
    title = "Student Information"
)
demo.launch()