import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


X = np.array([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]], dtype=float)
y = np.array([0, 0, 0, 1, 1, 1], dtype=float)

w = 0.0
b = 0.0
learning_rate = 0.1
epochs = 1000
n = len(X)

for epoch in range(epochs):
    z = X.dot(w) + b
    prediction = sigmoid(z)
    error = prediction - y
    cost = -(1 / n) * np.sum(y * np.log(prediction + 1e-9) + (1 - y) * np.log(1 - prediction + 1e-9))
    dw = (1 / n) * np.sum(error * X.reshape(n, 1))
    db = (1 / n) * np.sum(error)
    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 100 == 0:
        print('Epoch', epoch, 'Cost', cost)

print('\nFinal weight:', w)
print('Final bias:', b)


def predict(x):
    probability = sigmoid(w * x + b)
    label = 1 if probability >= 0.5 else 0
    return probability, label

new_input = 4.5
probability, result = predict(new_input)
print('Input:', new_input)
print('Probability:', probability)
print('Predicted class:', result)
