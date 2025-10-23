matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def print_upper_triangular_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(0,i+1):
            print(matrix[i][j], end=" ")
        print()

print_upper_triangular_matrix(matrix)