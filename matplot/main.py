import numpy as np
import matplotlib.pyplot as plt

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([10, 20, 30, 40, 50])

# plt.plot(x, y)
# plt.title("Line Plot")
# plt.xlabel("This is X Axis")
# plt.ylabel("This is Y Axis")
# plt.grid(True)
# plt.show()



# age = np.array([18, 22, 30, 35, 40])
# salary = np.array([20, 25, 40, 42, 55])

# plt.scatter(age, salary)
# plt.title("Scatter Plot")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.show()



# data = np.random.normal(50, 20, 200)

# plt.hist(data, bins=20)
# plt.title("Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()



classes = ["Cat", "Dog", "Bird"]
counts = [30, 45, 25]

plt.bar(classes, counts)
plt.title("Animal Counts")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()