nums = [1,1,2,2,3,4,4,7,9,9,9,10,12,12,22]

#Approach1 : BRUTE FORCE USING DICTIONARY
# def removes_duplicates(arr):
#     n = len(arr)
#     freq_dict = dict()
#     for i in range(n):
#         freq_dict[arr[i]] = 0
#
#     left = 0
#     for key in freq_dict:
#         arr[left] = key
#         left +=1
#
#     for i in range(left):
#         print(arr[i],end=" ")

#Approach1 : OPTIMAL SOLUTION USING TWO POINTER
def removes_duplicates(arr):
    n = len(arr)
    i = 0
    j = 1
    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    print(arr[:i+1])

# def removes_duplicates(arr):
#     n = len(arr)
#     left = 0
#
#     for i in range(n-1):
#         if arr[i] != arr[i+1]:
#             arr[left] = arr[i]
#             left += 1
#     if arr[n-1] != arr[n-2] :
#         arr[left] = arr[n-1]
#         left += 1
#
#
#     for i in range(left):
#         print(arr[i],end=" ")

removes_duplicates(nums)
