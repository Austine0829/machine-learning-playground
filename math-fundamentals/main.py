import numpy as np
# import matplotlib.pyplot as plt

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



###



# Matrix operations
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



###



#Derivative
# def f(x):
#     return x**2

# def power(x, power):
#     return x**(power-1)

# x = np.linspace(0, 5, 3)

# y = power(5)

# print(f(x))
# print(power(5, 3))

# 1st is common and 2nd is flip approach but still same.
# dw = 10
# db = 10

# y = 10
# y_pred = 8

# dw = np.mean(2 * (y_pred - y))
# print(dw)

# dw = -2 * np.mean((y - y_pred))
# print(dw)



###



# def f(x, y):
#     return x**2 + y**2

# # Compute partial derivatives (gradient)
# def grad_f(x, y):
#     df_dx = 2 * x
#     df_dy = 2 * y
#     return np.array([df_dx, df_dy])

# # Example point
# x, y = 2.0, 3.0
# gradient = grad_f(x, y)
# print("Gradient:", gradient)