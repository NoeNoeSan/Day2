import numpy as np

scores = np.array([45,60,72,88,95,67])
print("Total Scores: ",scores)
print("Shape: ",scores.shape)
print("Mean: ",np.mean(scores))
print("Media: ",np.median(scores))
print("Highest Score: ",np.max(scores))
print("Lowest Score: ",np.min(scores))
new_score = scores + 5
print("Update Scores: ",new_score)

two_dimension = np.array([[3,70],
                          [2,80],
                          [1,99]])
print("Two dimension: ", two_dimension)

