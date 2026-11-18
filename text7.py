import pandas as pd

# Missing value handle
df = pd.DataFrame({                             #another type of verification
    "Study_Hours": [2,4,None,3,7],              #row and columns must be the same numbers
    "Attendance" : [60,75,90,65,None],          # median()----odd number of list value so sort the numbers
    "Exam_score" : [45,65,85,55,92]
})

print("Missing value: ")
print(df.isnull().sum()) # show null value

df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"]).median()# fillna() is filling everything with median
print(df)
df["Attendance"] = df["Attendance"].fillna(df["Attendance"]).median()