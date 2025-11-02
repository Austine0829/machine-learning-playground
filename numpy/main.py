import numpy as np

data = np.array([[1, 2, 3], 
                 [4, 5, 6]])

dataTwo = np.array([[7, 8, 9],
                    [10, 11, 12],
                    [13, 14, 15]])

# print("\n", data.shape)

# # Row
# print("\n", data[0])

# # Column
# print("\n", data[:, 0])

# # No. Row to Access
# print("\n", data[:2])

# result = 2 * data

# print(result)

# print("Mean:", np.mean(data))
# print("Standard Deviation", np.std(data))

# dot = np.dot(data, dataTwo)

# print(dot)

random = np.random.rand(10)

np.random.shuffle(data)
print(data)