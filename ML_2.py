import joblib
import pandas as pd

loaded_model = joblib.load('ExamModel.joblib')#Use ExamModel.joblib which is already trained but must be in the same diectiory
print("Loaded Successfully")# Use load() function to call 

new_student = pd.DataFrame(
    {
        "study_hours": [4], # first features : data list
        "attendance": [65]
    }
    
    
)

prediction = loaded_model.predict(new_student)
print(prediction) 