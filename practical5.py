# Practical 5:
# Write a Python program using NumPy to:
# 1.	Create two matrices
# 2.	Perform matrix addition
# 3.	Perform matrix subtraction
# 4.	Perform matrix multiplication
# 5.	Find the transpose of both matrices


import numpy as np

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Addition
add = A + B
print("\nAddition of A and B:")
print(add)

# Subtraction
sub = A - B
print("\nSubtraction of A and B:")
print(sub)

# Multiplication (Matrix multiplication)
mul = np.dot(A, B)
print("\nMultiplication of A and B:")
print(mul)

# Transpose
print("\nTranspose of Matrix A:")
print(A.T)

print("\nTranspose of Matrix B:")
print(B.T)
