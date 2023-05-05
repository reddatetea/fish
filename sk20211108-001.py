from sklearn.linear_model import LinearRegression
import numpy as np

apple = np.array([155,156,157])
n = len(apple)
model = LinearRegression().fit(np.arange(n).reshape((n,1)),apple)
print(model.predict([[3],[4]]))