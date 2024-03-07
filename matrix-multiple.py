import numpy as bhai

# create matrices
A = bhai.array([[1, 2, 78], [3, 4], [5, 6]])
print("Matrix A - \n", A)

B = bhai.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix B - \n", B)

# multiple matrix

C = bhai.dot(A, B)
print("Matrix C - \n", C)

