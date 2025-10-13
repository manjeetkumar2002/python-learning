nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


#BRUTE FORCE APPROACH
# def rotate_90(nums):
#     rows = len(nums)
#     cols = len(nums[0])
#
#     result = [[0]*rows for i in range(cols)]
#     # print(result)
#     for row in range(rows):
#         for col in range(cols):
#             result[col][rows-row-1] = nums[row][col]
#     return result

# OPTIMAL APPROACH
def rotate_90(nums):
    rows = len(nums)
    cols = len(nums[0])
    # step1 : transpose the matrix
    for i in range(rows):
        for j in range(i+1,cols):
            nums[j][i], nums[i][j] = nums[i][j], nums[j][i]
    # step2 : reverse each row
    for i in range(rows):
        start = 0
        end = cols - 1
        while start < end:
            nums[i][start],nums[i][end] = nums[i][end],nums[i][start]
            start += 1
            end -= 1






def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()

rotate_90(nums)

print_matrix(nums)