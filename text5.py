import pandas as pd

data = {                            #python dictionary
    "Study_Hours": [2,4,6,3,7],
    "Attendance" : [60,75,90,65,95],
    "Exam_score" : [45,65,85,55,92]
}

df = pd.DataFrame(data) #change into pandas dataframe
print(data)
#print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())#mean,min,max,sdt,count