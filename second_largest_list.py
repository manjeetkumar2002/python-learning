# Approach1 : sorting
# TC : O(NlogN)
# def second_largest(nums):
#     nums.sort()
#     return nums[-2]

# Approach2 : using 2 loops
# # TC : O(2N)
# def second_largest(nums):
#     largest = float("-inf")
#     s_largest = float("-inf")
#     for num in nums:
#         largest = max(largest, num)
#
#     for num in nums:
#         if num > s_largest and num!=largest:
#             s_largest = num
#     return s_largest

# Approach3 : optimal solution ,single loop
# TC : O(N)
def second_largest(nums):
    largest = float("-inf")
    s_largest = float("-inf")
    for num in nums:
        if num > largest:
            s_largest = largest
            largest = num
        if num > s_largest and num != largest:
            s_largest = num
    return s_largest


nums = [43,45,98,65,76]
print(f"second largest element is {second_largest(nums)}")