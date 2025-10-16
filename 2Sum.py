nums = [5,9,1,2,4,15,6,3]
target = 13

#BRUTE FORCE USING 2 LOOPS
# def twoSum(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return [nums[i], nums[j]]
#     return [-1,-1]


#APPROACH2: USE DICTIONARY , TRAVERSE THE LIST AND CHECK IF TARGET-NUMS[I] IS PRESENT IN DICT OR NOT AND ALSO UPDATE THE DICT WHILE TRAVERSING
def twoSum(nums):
    n = len(nums)
    hash_map = dict()
    for i in range(n):
        complement = target - nums[i]
        if complement in hash_map:
            return [hash_map[complement],i]
        else :
            hash_map[nums[i]] = i
    return [-1,-1]


print(twoSum(nums))