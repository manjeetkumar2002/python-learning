nums1 = [1,2,3,4,5]
nums2 = [5,6,7,4,3,2]

# time complexity : O(N)
def is_sorted(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            print("Unsorted list")
            return False
    print("Sorted list")
    return True


is_sorted(nums1)
is_sorted(nums2)