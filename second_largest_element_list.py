nums = [2,3,5,6,7,1,8]

#brute force Time complexity O(NlogN)
# def second_largest(nums):
#     if len(nums) < 2:
#         return nums[0]
#     nums.sort()
#     return nums[len(nums)-2]

# Better Approach using two pass
# def second_largest(nums):
#     if len(nums) < 2:
#         return nums[0]
#     largest = float("-inf")
#     for num in nums:
#         largest = max(largest,num)
#     second_large = float("-inf")
#     for num in nums:
#         if num > second_large and num != largest:
#             second_large = num
#     return second_large

# optimal approach single pass
def second_largest(nums):
    if len(nums) < 2:
        return nums[0]
    largest = float("-inf")
    s_largest = float("-inf")

    for num in nums:
        if num > largest:
            s_largest = largest
            largest = num
        elif num > s_largest and num != largest:
            s_largest = num
    return s_largest

print(f"second largest element is {second_largest(nums)}")