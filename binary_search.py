nums = [2,3,4,5,6,1,5,7]
nums.sort()
print(nums)
# ITERATIVE APPROACH USING LOOPS
def binary_search(nums, key):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == key:
            return mid
        elif key < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
#RECURSIVE APPROACH
def bsearch(nums,key,low,high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == key:
        return mid
    elif key < nums[mid]:
        return bsearch(nums,key,low,mid-1)
    else:
        return bsearch(nums,key,mid+1,high)

index = bsearch(nums,3,0,len(nums)-1)
print(index)