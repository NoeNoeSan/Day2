import gradio as gr

def greet(name): # need to write a function that we use
    return f"Hello, {name}"

demo = gr.Interface(
    fn = greet, # fn = funtion you can't change the order in gr.Interface 
    inputs = gr.Textbox(label='Enter your name'),# accept input with Textbox
    outputs = gr.Textbox(label='Greeting'),
    title = "Greeting App"
)

demo.launch() # launch you can see UR 
#to stop runing click ctrl+C