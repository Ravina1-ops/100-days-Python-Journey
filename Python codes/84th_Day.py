Write a Python Program to Transpose a Matrix.
25/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
In [3]:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
# Function to transpose a matrix
def transpose_matrix(matrix):
rows, cols = len(matrix), len(matrix[0])
# Create an empty matrix to store the transposed data
result = [[0 for _ in range(rows)] for _ in range(cols)]
for i in range(rows):
for j in range(cols):
result[j][i] = matrix[i][j]
return result
# Input matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
# Transpose the matrix
transposed_matrix = transpose_matrix(matrix)
# Print the transposed matrix
for row in transposed_matrix:
print(row)