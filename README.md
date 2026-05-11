# NumPy-basics
This repository contains a series of Python scripts demonstrating the core capabilities of the NumPy library. These exercises focus on memory-efficient data structures, mathematical operations on arrays, and multi-dimensional data slicing—essential skills for Data Science and Machine Learning.
# 🔢 NumPy Basics for Data Science

This section covers the fundamental operations of **NumPy** (Numerical Python), the core library for scientific computing in Python. It is the foundation for almost all Data Science and Machine Learning projects.

## 📌 Core Concepts Covered

### 1. Array Creation
Creating high-performance multidimensional array objects (`ndarrays`).
- **Standard Arrays:** `np.array([1, 2, 3])`
- **Zero/One Initialization:** `np.zeros()`, `np.ones()`
- **Range Arrays:** `np.arange()` and `np.linspace()`

### 2. Array Attributes
Understanding the structure of your data:
- `.shape` – Dimensions of the array.
- `.ndim` – Number of axes.
- `.dtype` – Data type of elements (e.g., `int64`, `float32`).

### 3. Mathematical Operations
Performing element-wise calculations without using "for loops" (Vectorization):
- Addition, Subtraction, Multiplication, and Division.
- Square roots and Exponentials.
- Dot products for Matrix multiplication.

### 4. Indexing & Slicing
Accessing specific elements or "slices" of data from 1D and 2D arrays.
- `arr[0:5]` – Selecting the first five elements.
- `arr[row, col]` – Selecting specific values in a matrix.

---

## 🛠️ Essential Functions Used
| Function | Description |
| :--- | :--- |
| `np.reshape()` | Changes the shape of an array without changing data. |
| `np.mean()`, `np.median()` | Statistical analysis. |
| `np.transpose()` | Flips the axes of a matrix. |
| `np.random.rand()` | Generates random data for testing. |

---

## 💡 Why use NumPy?
NumPy arrays are faster and more memory-efficient than Python lists because they are stored in contiguous memory blocks. This is critical for handling the large datasets used in **Exploratory Data Analysis (EDA)**.
