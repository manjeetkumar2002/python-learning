nums = [7,7,7,7,7,7,7,1,2,3,4,5,7,7]
target = 1
def search(nums,target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2

        if nums[mid] == target:
            return mid

        if nums[low] == nums[mid] and nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        if nums[mid]<=nums[high]: # right side sorted
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