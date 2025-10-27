matrix = [[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,9]]


# my solution
def set_matrix_zeroes(matrix):
    # store the postition of zeroes in matrix
    positions = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                positions.append([i,j])

    for position in positions:
        row_idx = position[0]
        col_idx = position[1]
        # make this row elements all zeros
        for j in range(col):
            matrix[row_idx][j] = 0
        for i in range(row):
            matrix[i][col_idx] = 0

# OPTIMAL SOLUTION
def setZeroes(matrix):
    # store the postition of zeroes in matrix
    r = len(matrix)
    c = len(matrix[0])
    row_track = [0] * r
    col_track = [0] * c

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                row_track[i] = -1
                col_track[j] = -1

    for i in range(r):
        for j in range(c):
            if row_track[i] == -1 or col_track[j] == -1:
                matrix[i][j] = 0



def print_matrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()

setZeroes(matrix)
print_matrix(matrix)