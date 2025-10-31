import numpy as np


# Z-Score
# prices = np.array([100, 300, 500, 700, 900])

# mean = np.mean(prices)

# std = np.std(prices)

# normalized = (prices - mean) / std

# print("Normalized",normalized)



# Model Accuracy Evaluation
# y = np.array([1, 2, 3, 4, 5])
# y_predicted = np.array([1, 2, 3, 5 ,4])
# correct = 0

# for i in range(5):
#     if y[i] == y_predicted[i]:
#         correct += 1

# print("Accuracy:", correct / len(y_predicted))



# --- Step 1: Example dataset ---
data = np.array([1, 12, 14, 18, 19, 20, 21, 22, 50])  # 100 looks suspicious

# --- Step 2: Compute quartiles ---
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)

# --- Step 3: Compute IQR ---
IQR = Q3 - Q1

# --- Step 4: Define normal range ---
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# --- Step 5: Detect outliers ---
outliers = data[(data < lower_bound) | (data > upper_bound)]

# --- Step 6: Print results ---
print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("IQR:", IQR)
print("Normal Range:", (lower_bound, upper_bound))
print("Outliers:", outliers)