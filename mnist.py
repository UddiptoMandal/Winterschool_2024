import numpy as np
import keras
# from tensorflow.keras import layers, models
# from tensorflow.keras.datasets import mnist
# from tensorflow.keras.utils import to_categorical


(x_train1, y_train), (x_test1, y_test) = keras.datasets.mnist.load_data()
assert x_train1.shape == (60000, 28, 28)
assert x_test1.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)
print(x_train1)
print(x_test1)
print(y_train)
print(y_test)
# x_train = np.zeros((60000, 784))
# x_test = np.zeros((10000, 784))
# for i in range (60000):
#   x_train[i] = x_train1[i].flatten()
# for i in range (10000):
#   x_test[i] = x_test1[i].flatten()
# # print(x_train)
# # print(x_test)

# def init_params(predictors):
#     np.random.seed(0)
#     weights = np.random.rand(predictors, 1)
#     biases = np.ones((1,1))
#     return [weights, biases]
# # print(init_params(784))

# def forward(params, x):
#     weights, biases = params
#     prediction = x @ weights + biases
#     pred = 1/(1+np.exp(-prediction))  #sigmoid
#     return pred

# def mse(actual, predicted):
#     return (np.mean(actual-predicted)**2)/2
# def mse_grad(actual, predicted):
#     return predicted - actual

# def backward(params, x, alpha, grad):
#     w_grad = (x.T / x.shape[0]) @ grad   #divide by num of rows in x as in batch gradient descent, avoid too large update if x val large
#     b_grad = np.mean(grad, axis = 0)  #grad of b = grad itself

#     params[0] = params[0] - alpha * w_grad
#     params[1] = params[1] - alpha * b_grad
#     return params

# alpha = 1e-3
# iter = 10

# params = init_params(x_train.shape[1])
# for i in range(iter):
#     predictions = forward(params, x_train)
#     grad = mse_grad(y_train, predictions)
#     params = backward(params, x_train, alpha, grad)
#     if i % (iter/10) == 0:
#         print(f"validation {i}")
#         predictions = forward(params, x_test)
#         loss = mse(y_test, predictions)
#         print(loss)
# print(params)
