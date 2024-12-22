# Matrix Operations Library
# Description: Build a library for matrix operations using NumPy. The library should define a Matrix class that provides operations like addition, multiplication, transpose, determinant, and inverse.
# Key Features:
# Overload operators (+, *, ==) for matrix operations.
# Use NumPy for actual matrix calculations.
# Include error handling for invalid operations (e.g., non-conformable matrices).
# Skills Gained:
# OOP principles: classes, encapsulation, and operator overloading.
# NumPy for matrix manipulations.


import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.matrix + other.matrix)
        raise TypeError("Operand must be an instance of Matrix.")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.matrix @ other.matrix)  # Matrix multiplication
        raise TypeError("Operand must be an instance of Matrix.")

    def transpose(self):
        return Matrix(self.matrix.T)

    def det(self):
        return np.linalg.det(self.matrix)  # Returns scalar

    def inverse(self):
        try:
            return Matrix(np.linalg.inv(self.matrix))
        except np.linalg.LinAlgError as e:
            raise ValueError("Matrix is not invertible.") from e

    def __str__(self):
        return str(self.matrix)

# Example usage
m = Matrix(np.array([[1, 2, 3]]))
k = Matrix(np.array([[4, 5, 6]]))
j = m + k
print("Addition Result:\n", j)

# Matrix multiplication
d = Matrix(np.array([[1, 2], [3, 4]]))
e = Matrix(np.array([[5, 6], [7, 8]]))
f = d * e
print("\nMultiplication Result:\n", f)

# Transpose
print("\nTranspose of d:\n", d.transpose())

# Determinant
g = Matrix(np.array([[2, 3], [1, 4]]))
print("\nDeterminant of g:", g.det())

# Inverse
try:
    print("\nInverse of g:\n", g.inverse())
except ValueError as err:
    print(err)


