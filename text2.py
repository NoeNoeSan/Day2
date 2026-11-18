import numpy as np

data = np.array([[2,60,]
                 [4,70],
                 [6,90]])

print(data)
print("Shape", data.shape) # 3 lists , 2 dimension
print("First student",data[0])# 2 60
print("Study Hours",data[:,0])# 2 4 6