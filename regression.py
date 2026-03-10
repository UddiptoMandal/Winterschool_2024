import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

teams = pd.read_csv("teams.csv")
x = teams[["athletes"]].copy()
y = teams[["medals"]].copy()
plt.plot(x, y, 'o')
x["intercept"] = 1
x = x[["intercept", "athletes"]]
xt = x.T
B = np.linalg.inv(xt @ x) @ xt @ y
B.index = x.columns
print(B)
pred = x @ B
print(pred)
plt.plot(x,pred)
plt.show()
SSR = ((y-pred)**2).sum()
SST = ((y-y.mean()) ** 2).sum()
error = 1- (SSR/SST)
print(error)

teams = pd.read_csv("teams.csv")
print(teams)
x = teams[["athletes", "events", "age", "height", "weight"]].copy()
y = teams[["medals"]].copy()

x["intercept"] = 1
x = x[["intercept", "athletes", "events", "age", "height", "weight"]]
xt = x.T
B = np.linalg.inv(xt @ x) @ xt @ y
B.index = x.columns
# print(B)
pred = x @ B
print(pred)

SSR = ((y-pred)**2).sum()
SST = ((y-y.mean()) ** 2).sum()
error = 1- (SSR/SST)
print('Error:', error)