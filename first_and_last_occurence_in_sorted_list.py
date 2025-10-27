nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]

def lower_bound(nums,target):
    low = 0
    high = len(nums)-1
    lb = len(nums)
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>=target:
            lb = mid
            high = mid-1
        else:

            low = mid+1
    return lb

def upper_bound(nums,target):
    low = 0
    high = len(nums)-1
    ub = len(nums)
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>target:
            ub = mid
            high = mid-1

        else:
            low = mid+1
    return ub

def first_last_occurrence(nums,target):
    lb = lower_bound(nums,target)
    if lb == -1:
        return [-1,-1]
    ub = upper_bound(nums,target)
    return [lb,ub-1]

print(f"first and last occurrence is : {first_last_occurrence(nums,3)}")