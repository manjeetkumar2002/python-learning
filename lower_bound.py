# LOWER BOUND : smallest index such that nums[i]>=target
nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = 1

def lower_bound(nums,target):
    low = 0
    high = len(nums)-1
    result = len(nums)
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>=target:
            result = nums[mid]
            high = mid-1
        else:
            low = mid+1
    return result

print(lower_bound(nums,target))