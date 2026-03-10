import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Generate 30 points around a line y = 0.8x + 5 with some noise
tmax = np.linspace(20, 40, 30)
tmax_tomorrow = 0.8 * tmax + 5 + np.random.normal(0, 2, size=30)  # Adding noise

data = pd.DataFrame({
    "tmax": tmax,
    "tmax_tomorrow": tmax_tomorrow
})

print(data)
print(data.head(5))

PREDICTORS = ["tmax"]
TARGET = "tmax_tomorrow"


split_data = np.split(data, [int(.7 * len(data)), int(.85 * len(data))])
(train_x, train_y), (valid_x, valid_y), (test_x, test_y) = [
    [d[PREDICTORS].to_numpy(), d[[TARGET]].to_numpy()] for d in split_data]

plt.plot(train_x, train_y, 'o')
plt.xlabel("tmax")
plt.ylabel("tmax_tomorrow")
plt.title("Temperature Relationship")

def init_params(predictors):
    np.random.seed(0)
    weights = np.random.rand(predictors, 1)
    biases = np.ones((1,1))
    return [weights, biases]
# print(init(3))

def forward(params, x):
    weights, biases = params
    prediction = x @ weights + biases
    return prediction

def mse(actual, predicted):
    return (np.mean(actual-predicted)**2)/2
def mse_grad(actual, predicted):
    return predicted - actual

def backward(params, x, alpha, grad):
    w_grad = (x.T / x.shape[0]) @ grad   #divide by num of rows in x as in batch gradient descent, avoid too large update if x val large
    b_grad = np.mean(grad, axis = 0)  #grad of b = grad itself

    params[0] = params[0] - alpha * w_grad
    params[1] = params[1] - alpha * b_grad
    return params

alpha = 1e-4
iter = 1000

params = init_params(train_x.shape[1])
for i in range(iter):
    predictions = forward(params, train_x)
    grad = mse_grad(train_y, predictions)
    params = backward(params, train_x, alpha, grad)
    if i % (iter/10) == 0:
        print(f"validation {i}")
        predictions = forward(params, valid_x)
        loss = mse(valid_y, predictions)
        
        print(loss)
plt.plot(train_x, predictions, label = "fit", color = "green")
plt.title("Fitted data")
plt.show()
# plt.plot(data['tmax'], predictions, 'green')
# plt.show()