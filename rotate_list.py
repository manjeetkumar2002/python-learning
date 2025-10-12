nums = [1,2,3,4,5,6,7]

# USING SLICING
def rotate1(nums):
    n = len(nums)
    nums = nums[-1:] + nums[:n-1]
    print(nums)
# USING LOOP
def rotate2(nums):
    n = len(nums)
    last_num = nums[-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = last_num
    print(nums)

rotate2(nums)
