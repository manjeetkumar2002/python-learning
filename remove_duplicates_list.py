nums = [1,1,2,2,3,4,4,7,8,8,8,10]

# BRUTE FORCE :USING DICTIONARY BECAUSE IT ONLY CONTAINS UNIQUE KEYS IN ORDER
# def remove_duplicates(nums):
#     hashmap = {}
#     for num in nums:
#         hashmap[num] = 0
#     index = 0
#     for key in hashmap:
#         nums[index] = key
#         index += 1
#     return index

def remove_duplicates(nums):
    left = 0
    if len(nums)==1:
        return 1
    for i in range(left+1,len(nums)):
        if nums[i] != nums[left]:
            left += 1
            nums[left], nums[i] = nums[i], nums[left]

    return left+1

new_size = remove_duplicates(nums)
for i in range(new_size):
    print(nums[i],end = " ")