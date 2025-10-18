import numpy as np

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