#FLOOR VALUE : largest number in array <= target
#CEIL VALUE : smallest number in array >= target
nums = [3,4,4,4,8,9,9,10,12,12,14,15]

def floor_ceil(nums,target):
    n = len(nums)
    floor = -1
    ceil = -1
    low,high = 0,n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid]==target:
            return [nums[mid],nums[mid]]
        elif nums[mid]<target:
            floor = nums[mid]
            low = mid+1
        else:
            ceil = nums[mid]
            high = mid-1

    return [floor,ceil]

print(floor_ceil(nums,5))
