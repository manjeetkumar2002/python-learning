nums = [11,15,20,1,4,5,6,8,9,10]
target = 15
def search(nums,target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2

        if nums[mid] == target:
            return mid
        elif nums[mid]<=nums[high]: # right side sorted
            #target is in sorted part ?
            if target >= nums[mid] and target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
        else: # left side sorted
            if target >= nums[low] and target <= nums[mid]:
                high = mid-1
            else:
                low = mid+1
    return -1

print(search(nums,target))