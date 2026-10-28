import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(output):
    return output * (1 - output)

# XOR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Seed for reproducible weights
np.random.seed(42)

# Network architecture: 2 inputs -> 4 hidden neurons -> 1 output neuron
W1 = np.random.uniform(-1, 1, (2, 4))
b1 = np.zeros((1, 4))
W2 = np.random.uniform(-1, 1, (4, 1))
b2 = np.zeros((1, 1))

learning_rate = 0.5
epochs = 10000

for epoch in range(epochs):
    # Forward pass
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(final_input)

    # Backpropagation (Chain Rule)
    error = y - predicted_output
    d_predicted = error * sigmoid_derivative(predicted_output)

    error_hidden = d_predicted.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Weight and bias updates
    W2 += hidden_output.T.dot(d_predicted) * learning_rate
    b2 += np.sum(d_predicted, axis=0, keepdims=True) * learning_rate
    W1 += X.T.dot(d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

print("ANN XOR Predictions (Rounded):")
print(np.round(predicted_output, 3))