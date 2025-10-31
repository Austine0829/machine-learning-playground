import numpy as np
import matplotlib.pyplot as plt

# # Scalars 

# age = 24
# height = 170
# weight = 100

# print("Age:", age)
# print("Height:", height)
# print("Weight:", height)

# BMI = weight / ((height / 100) ** 2 )

# print("Body Mass Index:", BMI)


# # Vectors

# numbers = np.array([1, 2 ,3, 4, 5, 6])

# result = np.median(numbers)

# print("result:", result)


# # MATRIX
# people = np.array([
#     [25, 170, 65.5],
#     [30, 180, 75.0],
#     [22, 160, 55.0],
#     [23, 164, 57.0]
# ])

# print("Matrix (people):\n", people)

# # Shape (rows, cols)
# print("Shape:", people.shape)  # (3 samples, 3 features)

# # Access a row (one person)
# print("First person:", people[0])

# # Access a column (one feature across all people)
# print("All heights:", people[:, 1])

# # Compute column means (average of each feature)
# column_means = np.mean(people, axis=0)
# print("Average [Age, Height, Weight]:", column_means)


# # Matrix operations
# a_matrix = np.array([[1, 2],
#                      [3, 4]])

# b_matrix = np.array([[5, 6],
#                      [7, 8]])

# add = a_matrix + b_matrix
# subract = np.subtract(a_matrix, b_matrix)
# dotProduct = np.dot(a_matrix, b_matrix)
# transpose = np.transpose(a_matrix)
# inverse = np.linalg.inv(a_matrix)

# matrixIdentity = np.dot(a_matrix, inverse)

# print("\nSum of A and B Matrices\n",add)
# print("\nSubract of A and B Matrices\n", subract)
# print("\nDot Product of A and B Matrices\n", dotProduct)
# print("\nTranspose Matrix A\n", transpose)

# print("\nInverse of Matrix A\n", inverse)
# print("\n Matrix A Identity\n", np.round(matrixIdentity, 10))

# Function
def f(x):
    return x**2

# Derivative
def f_prime(x):
    return 2*x

# Points
x = np.linspace(-5, 5, 100)
y = f(x)

# Tangent at x0
x0 = 2
y0 = f(x0)
slope = f_prime(x0)
tangent = slope * (x - x0) + y0

# Plot
plt.plot(x, y, label="f(x) = x^2")
plt.plot(x, tangent, label=f"Tangent at x={x0}", linestyle='--')
plt.scatter(x0, y0, color='red')  # Point of tangency
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Derivative Visualization")
plt.grid(True)
plt.show()
