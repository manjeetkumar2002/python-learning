matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

# USING EXTRA SPACE
def transpose_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result_matrix = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result_matrix[j][i] = matrix[i][j]
    print_matrix(result_matrix)


# USING SWAPING
def transpose_matrix2(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(i+1,m):
            matrix[j][i] = matrix[i][j]
    print_matrix(matrix)

transpose_matrix2(matrix)

