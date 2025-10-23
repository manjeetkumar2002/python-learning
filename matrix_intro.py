matrix = [[1,2,3],[4,5,6],[7,8,9]]

def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

print_matrix(matrix)