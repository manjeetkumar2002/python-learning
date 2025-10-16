nums = [0,3,0,1,0,4,0,0,]

# APPROACH 1:
# STEP1: STORE THE NON ZEROES IN A TEMP ARRAY
# STEP2: UPDATE THIS ELEMENTS OF TEMP FROM THE STARTING OF NUMS ,FROM INDEX 0 TO LEN(TEMP)-1
# STEP3: NOW UPDATE THE REST OF  ELEMENTS OF NUMS TO 0 FROM INDEX LEN(TEMP) TO N-1
# def moveZeroesToEnd(nums):
#     temp = []
#     n = len(nums)
#     # store non zeroes
#     for i in range(n):
#         if nums[i]>0:
#             temp.append(nums[i])
#     # update the nums
#     for i in range(0,len(temp)):
#         nums[i] = temp[i]
#
#     for i in range(len(temp),n):
#         nums[i] = 0

# APPROACH 2 :
# PLACE THE NON ZEROES TO THEIR CORRECT POSITION WHILE TRAVERSING THE LIST
# USE A LEFT POINTER WHICH TRACK THE POSITION OF THE NEXT NONZERO ELEMENT
def moveZeroesToEnd(nums):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == 0:
            break
        i += 1
    if i == len(nums):
        return
    j = i + 1
    while j < n:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1


moveZeroesToEnd(nums)
print(nums)