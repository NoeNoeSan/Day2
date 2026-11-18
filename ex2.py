import pandas as pd

df = pd.read_csv('data/ex_student.csv')

print(df.head())
print(df.isnull().sum())
X = df[["study_hours","attendance","previous_score"]]
y = df["exam_score"]
print(X)
print(y)