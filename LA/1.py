# Linear Algebra
# Taufeeq Riyaz - 1RVU23CSE506

import numpy as rvu

# (a) Matrix creation
def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Enter element at position ({i+1}, {j+1}) - ")))
        matrix.append(row)
    return matrix

# (b) Matrix addition
def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices should have same dimensions for addition"
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# (c) Matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Number of columns in first matrix should be equal to number of rows in second matrix"
    
    result = rvu.zeros((len(matrix1), len(matrix2[0])))
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# (d) Transpose of a Matrix
def matrix_transpose(matrix):
    return rvu.transpose(matrix)

# (e) Find the determinant of a matrix
def matrix_determinant(matrix):
    return rvu.linalg.det(matrix)


# Main Function go brrrr

print("Linear Algebra Activity 1 - Taufeeq Riyaz")

rows = int(input("Enter the number of rows - "))
cols = int(input("Enter the number of columns - "))

print("Enter elements of matrix 1 -")
matrix1 = create_matrix(rows, cols)

print("Enter elements of matrix 2 -")
matrix2 = create_matrix(rows, cols)

print("Matrix 1 -")
print(rvu.array(matrix1))
print("Matrix 2 -")
print(rvu.array(matrix2))

print("Matrix addition -")
print(matrix_addition(matrix1, matrix2))

print("Matrix multiplication -")
print(matrix_multiplication(matrix1, matrix2))

print("Transpose of Matrix 1 -")
print(matrix_transpose(matrix1))

print("Determinant of Matrix 1 -")
print(matrix_determinant(matrix1))

