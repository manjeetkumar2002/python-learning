nums = [-2,1,-3,4,-1,2,1,-4,4]

# BRUTE FORCE : GENERATE ALL SUBARRAY AND FIND THEIR SUM
def func(nums):
    n = len(nums)
    maxi = float("-inf")

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            maxi = max(maxi,sum)
    return maxi
# OPTIMAL APPROACH : KADANE'S ALGORITHM
def maxSubArray(nums):
    n = len(nums)
    maxi = float("-inf")
    sum = 0
    for i in range(n):
        sum += nums[i]
        maxi = max(sum,maxi)
        if sum <0:
            sum = 0
    return maxi

print(maxSubArray(nums))