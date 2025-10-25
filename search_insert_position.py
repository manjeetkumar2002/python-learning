nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = 4

def search_position(nums,target):
    low = 0
    high = len(nums)-1
    pos = len(nums)
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>=target:
            pos = mid
            high = mid-1
        else:
            low = mid+1
    return pos

print(search_position(nums,target))