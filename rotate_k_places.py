nums = [1,2,3,4,5,6,7,8,9]
k = 5

# APPROACH 1 : POP K ELEMENTS FROM LAST ONE BY ONE AND INSERT THEM AT INDEX 0
# def rotateKPlaces(nums,k):
#     for i in range(k):
#         e = nums.pop()
#         nums.insert(0,e)

# APPROACH 2 : IF K VALUE IS GREATER THAN LENGTH OF LIST USE THIS OPTIMISED VERSION OF THE ABOVE APPROACH
# def rotateKPlaces(nums,k):
#     k = k % len(nums)
#     for i in range(k):
#         e = nums.pop()
#         nums.insert(0,e)


# APPROACH 3 : USE SLICING PLACE THE SUBARRAY FROM INDEX (N-K TO N) AT STARTING OF SUBARRAY (0 TO N-K-1)
# def rotateKPlaces(nums, k):
#     k = k%len(nums)
#     n = len(nums)
#     nums[:] = nums[n-k:] + nums[:n-k]

# APPROACH 4 : REVERSE THE SUBARRAY (N-K TO N) AND THEN REVERSE SUBARRAY (0 TO N-K-1)
# AND THEN AT LAST REVERSE THE WHOLE ARRAY (0 TO N)
def rotateKPlaces(nums, k):
    k = k%len(nums)
    n = len(nums)
    reverse(nums,n-k,n-1)
    reverse(nums,0,n-k-1)
    reverse(nums,0,n-1)

def reverse(nums,start,end):
    while start < end:
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1
rotateKPlaces(nums,k)
print(nums)