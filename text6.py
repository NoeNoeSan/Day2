import pandas as pd

data = {                            #python dictionary
    "Study_Hours": [2,4,6,3,7],
    "Attendance" : [60,75,90,65,95],
    "Exam_score" : [45,65,85,55,92]
}

df = pd.DataFrame(data) #change into pandas dataframe

X = df[["Study_Hours","Attendance"]] # features/input
y = df["Exam_score"] #label/target/output/outcome/prediction

print("features")#ဒေါင်လိုက်ခွဲတာ
print(X)