nums = [1,2,3,-4,-5,-6]

# BRUTE FORCE
# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY:O(N)
# def rearrange(nums):
#     n = len(nums)
#     pos_list = []
#     neg_list = []
#     # store elements into pos_list and neg_list
#     for num in nums:
#         if num<0:
#             neg_list.append(num)
#         else:
#             pos_list.append(num)
#     # Place this element alternatively in nums
#     for i in range(0,len(pos_list)):
#        nums[2*i] = pos_list[i]
#        nums[2*i+1] = neg_list[i]
#     print(nums)
#
# rearrange(nums)

# OPTIMAL SOLUTION
def rearrange(nums):
    n = len(nums)
    res = [0]*n
    pos_index = 0
    neg_index = 1

    for num in nums:
        if num>=0:
            res[pos_index] = num
            pos_index += 2
        else:
            res[neg_index] = num
            neg_index += 2
    print(res)

rearrange(nums)

