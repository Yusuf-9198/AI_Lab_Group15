import numpy as np


def activation(value):
    return 1 if value >= 0 else 0


X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=float)

y = np.array([0, 0, 0, 1], dtype=float)

weights = np.zeros(2)
bias = 0.0
learning_rate = 0.1
epochs = 10

for _ in range(epochs):
    for sample, target in zip(X, y):
        z = np.dot(sample, weights) + bias
        prediction = activation(z)
        error = target - prediction
        weights += learning_rate * error * sample
        bias += learning_rate * error

print('Training completed.')
print('Weights:', weights)
print('Bias:', bias)

print('\nPredictions:')
for sample in X:
    z = np.dot(sample, weights) + bias
    prediction = activation(z)
    print(sample, '->', prediction)
