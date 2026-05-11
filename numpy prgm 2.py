import numpy as np

data = np.array([1, 2, 3])

# Vectorized math
print(data + 10)  # [11, 12, 13]
print(data * 2)   # [2, 4, 6]
print(data ** 2)  # [1, 4, 9]

# Operations between two arrays
b = np.array([10, 20, 30])
print(data + b)   # [11, 22, 33]