import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data/mini_pj_student.csv')
print(df.head())

X = df[['study_hours','attendance']]
y = df['exam_score']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
print("Train size",len(X_train))
print("Test size",len(X_test))

model = LinearRegression()
model.fit(X_train,y_train)
print("Training complete")

y_predict = model.predict(X_test)

print("Actual score",y_test.tolist())
print("Predict score",y_predict.tolist())

new_stu = pd.DataFrame(
    {
        'study_hours': [9],
        'attendance' : [77]
    }
)

prediction_score = model.predict(new_stu)
print("Predicted score for new student :",prediction_score)

import joblib #store trained data  not to train again and again

joblib.dump(model,'MiniPjExamModel.joblib')#save as ExamModel.joblib (store use dump() function)
print("Model save successful")

