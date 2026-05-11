import numpy as np

# Create a simple 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array (Matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Generate an array of zeros, ones, or a range
zeros = np.zeros((2, 3))       # 2x3 matrix of 0.0
step_arr = np.arange(0, 10, 2) # [0, 2, 4, 6, 8]

print("1D Array:", arr_1d)
print("Matrix Shape:", matrix.shape)