from sklearn.model_selection import train_test_split # train_test_split -- classify data 

from sklearn.linear_model import LinearRegression # range data

import pandas as pd

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8], # first features : data list
    "attendance": [50, 55, 60, 65, 70, 80, 85, 95],# rows = 8 and columns = 3 (features)
    "exam_score": [35, 40, 48, 55, 60, 72, 80, 90]# label
})

X = df[["study_hours","attendance"]] # 2 features so double [[]]
y = df["exam_score"]# only y because y is label,target,prediction
# To train you have to give both X and y but can't give all of the data otherwise we don't have to test wherther it is learning or not
# 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25) # variables careful ('train_test_split' step)
#test_size = unseen percent or traing precent of data 


print("Training Size", len(X_train))
print("Test Size",len(X_test))

# training

model = LinearRegression()

model.fit(X_train, y_train)# model training step 
print("Model Train complete.")

# prection using testing data

y_predict = model.predict(X_test)

print("Actual score")
print(y_test.tolist())

print("Predict score")
print(y_predict.tolist())

# test with unseen data
new_student = pd.DataFrame(
    {
        "study_hours": [5], # first features : data list
        "attendance": [80]
    }
    
    
)
prediction_score = model.predict(new_student)
print("Predicted score for new student :",prediction_score)

import joblib #store trained data  not to train again and again

joblib.dump(model,'ExamModel.joblib')#save as ExamModel.joblib (store use dump() function)
print("Model save successful")