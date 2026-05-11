import numpy as np

# Create a 3x3 matrix
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Get a specific element: row 0, column 1
print("Element (0,1):", matrix[0, 1]) 

# Get an entire row
print("First row:", matrix[0, :])

# Slice a sub-matrix (First 2 rows, First 2 columns)
print("Sub-matrix:\n", matrix[:2, :2])