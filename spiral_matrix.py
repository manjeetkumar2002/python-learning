matrix = [[1,2,3,4,5,6],
        [20,21,22,23,24,7],
        [19,32,33,34,25,8],
        [18,31,36,35,26,9],
        [17,30,29,28,27,10],
        [16,15,14,13,12,11]
        ]

def spiral_print(matrix):
    r = len(matrix)
    c = len(matrix[0])
    start_row = 0
    start_col = 0
    end_row = r-1
    end_col = c-1
    total = r*c
    count = 0
    result = []
    while count<total:
        #print the top row right
        j=start_col
        while count<total and j<=end_col:
            result.append(matrix[start_row][j])
            count=count+1
            j+=1
        start_row += 1
        #print the last col down
        i = start_row
        while count < total and i <=end_row:
            result.append(matrix[i][end_col])
            count = count + 1
            i += 1
        end_col -= 1
        #print the last row left
        j = end_col
        while count<total and j>=start_col:
            result.append(matrix[end_row][j])
            count = count + 1
            j-=1
        end_row -= 1
        #print the first col up
        i = end_row
        while count<total and i>=start_row:
            result.append(matrix[i][start_col])
            count = count + 1
            i-=1
        start_col += 1
    return result

result = spiral_print(matrix)
print(result)