import numpy as np

data = np.array([[-5, 2, 10],
                 [0, -3, 5],
                 [7, 4, -2]])

# Min-Max Scaling to [0,1]
data_min = data.min(axis=0)
data_max = data.max(axis=0)
minmax_scaled = (data - data_min) / (data_max - data_min)

# Standard Scaling (mean=0, std=1)
mean = data.mean(axis=0)
std = data.std(axis=0)
standard_scaled = (data - mean) / std

# Sigmoid
sigmoid = 1 / (1 + np.exp(-data))

# ReLU
relu = np.maximum(0, data)

print("Original Data:\n", data)
print("\nMin-Max Scaled Data:\n", minmax_scaled)
print("\nStandard Scaled Data:\n", standard_scaled)
print("\nSigmoid:\n", sigmoid)
print("\nReLU:\n", relu)
