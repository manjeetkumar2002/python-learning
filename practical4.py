# Practical 4:
# Write a Python program using NumPy to:
# 1.	Create a 3-dimensional array of size (2, 2, 3)
# 2.	Display the array
# 3.	Find its shape, size, and dimension
# 4.	Access one element using indexing
#
# NOTE : Knowledge on numpy
# Question	Answer
# What is NumPy?	Library for numerical computing
# What is a 3D array?	Array with 3 axes
# What does shape give?	Structure of array
# What does ndim give?	Number of dimensions
# What does size give?	Total elements

import numpy as np
# Create 3D array of size (2, 2, 3)
arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print("3D Array:")
print(arr)

print("\nShape of array:", arr.shape)
print("Size of array:", arr.size)
print("Dimension of array:", arr.ndim)

# Accessing element (2nd block, 1st row, 3rd column)
print("\nElement at index [1][0][2]:", arr[1][0][2])
