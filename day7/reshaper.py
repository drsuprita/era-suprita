import numpy as np

data = np.arange(24)
data = data.reshape(4, 3, 2)
data = data.transpose(0, 2, 1)

print(data.shape)
print(data)
