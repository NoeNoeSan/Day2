import gradio as gr
import joblib
import pandas as pd

loaded_model = joblib.load('MiniPjExamModel.joblib')#Use ExamModel.joblib which is already trained but must be in the same diectiory
print("Loaded Successfully")# Use load() function to call 

new_student = pd.DataFrame(
    {
        "study_hours": [4], # first features : data list
        "attendance": [65]
    }
    
    
)

prediction = loaded_model.predict(new_student)
print(prediction) 

def display(a,b):
    return a+b

demo = gr.Interface(
    fn = display, # fn = funtion you can't change the order in gr.Interface 
    inputs = [
                gr.Number(label = "Enter your study_hours :"),
                gr.Number(label = "Enter your attendance")
            ],
    outputs = gr.Number(label='Final Result Prediction'),
    title = "Student Score"
)

demo.launch()