import numpy as np
import matplotlib.pyplot as plt

x = np.array([50, 100, 150, 200, 250])
y = np.array([100, 200, 300, 400, 500])
w = np.random.rand()
b = np.random.rand()
lr = 0.000001
epoch = 200

for i in range(epoch):
    linear = w * x + b

    MSE = np.mean((linear - y) ** 2)

    dw = np.mean((linear - y) * x)
    db = np.mean((linear - y))

    w -= lr * dw
    b -= lr * db

print(f"\nWeight: {w}")
print(f"Bias: {b}")
print(f"MSE: {MSE}")

test_value = 50
test_prediction = w *  test_value + b
print(f"Test Result: {test_prediction}")

plt.text(150, 150, f"MSE: {MSE}", fontsize=12, color='black')

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, w * x + b, color='red', label='Prediction Line')
plt.ylabel("Prices")
plt.xlabel("Sqr Meters")
plt.legend()
plt.grid(True)
plt.show()