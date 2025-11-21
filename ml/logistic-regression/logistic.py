import numpy as np
import matplotlib.pyplot as plt

X = np.array([10, 2, 5, 3, 6, 8, 9, 13]) % 2
X_orig = np.array([10, 2, 5, 3, 6, 8, 9, 13])
y = np.array([1, 1, 0, 0, 1, 1, 0, 0])

label = {0: "Odd", 1: "Even"}

weight = np.random.rand()
bias = np.random.rand()
learning_rate = 0.1
epochs = 100

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for i in range(epochs):
    z = weight * X + bias
    y_pred = sigmoid(z)

    dw = np.mean((y_pred - y) * X)
    db = np.mean(y_pred - y)

    weight -= learning_rate * dw
    bias -= learning_rate * db

testing_set = np.array([[22],
                        [31],
                        [1002]])

preprocessed_testing_set = np.array([[22],
                                     [31],
                                     [1002]]) % 2

probability = sigmoid(weight * preprocessed_testing_set + bias)
result = (probability >= .5).astype(int)

for i in range(len(result)):
    print(f"{testing_set[i]} is {label[result.flatten()[i]]}")

plt.scatter(X_orig, y, color="red", label="Data Points")
plt.plot(X_orig, (sigmoid(weight * X + bias) >= .5).astype(int), color="Green", label="Learned Line")
plt.xlabel("X Feature Values")
plt.ylabel("Y Feature Values")
plt.legend()
plt.show()