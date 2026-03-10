import random
import numpy as np
import matplotlib.pyplot as plt

m=random.randint(-40,40)
c=random.randint(-20,20)

n = 25
xVal = np.linspace(-10, 10, n)
yVal = m * xVal + c + np.random.normal(0, 16, n)

epochs=100
mPred = random.uniform(-50, 50)
cPred = random.uniform(-30, 30)
alpha = 0.001
costArr = []

for i in range(epochs):
    yPred=mPred*xVal+ cPred
    error=(yPred-yVal)
    cost=np.mean(error**2)
    costArr.append(cost)
    
    dm = (2/n) * np.sum(error * xVal)
    dc = (2/n) * np.sum(error)
    mPred -= alpha * dm
    cPred -= alpha * dc

    
plt.figure(figsize=(12, 5))
plt.scatter(xVal, yVal, label='Noisy Data')
plt.plot(xVal, mPred * xVal + cPred, color='red', label='Best Fit Line')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
print(m,c)
print(mPred,cPred)

plt.subplot(1, 2, 2)
plt.plot(range(epochs), costArr, label='Loss')
plt.xlabel('epochs')
plt.ylabel('Loss')
plt.title('Loss vs epochs')
plt.legend()

plt.show()