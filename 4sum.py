nums = [1,0,-1,0,-2,2]

# BRUTE FORCE USING 4 LOOPS
# def _4sum(nums):
#     my_set = set()
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 for l in range(k+1,n):
#                     sum = nums[i] + nums[j] + nums[k] + nums[l]
#                     if sum == 0:
#                         temp = [nums[i],nums[j],nums[k],nums[l]]
#                         temp.sort()
#                         my_set.add(tuple(temp))
#     print(my_set)
#
# _4sum(nums)

# BETTER SOLUTION USING HASHSET
# fourth_element = target - (nums[i]+nums[j]+nums[k])
# def _4sum(nums):
#     my_set = set()
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             hash_set = set()
#             for k in range(j+1,n):
#                 forth_element = - (nums[i]+nums[j]+nums[k])
#                 if forth_element in hash_set:
#                     temp = [nums[i],nums[j],nums[k],forth_element]
#                     temp.sort()
#                     my_set.add(tuple(temp))
#                 hash_set.add(nums[k])
#
#     print(my_set)


#OPTIMAL SOLUTION : USING TWO POINTER
def _4sum(nums,target=0):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(0,n):
        if i > 0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            k = j+1
            l = n-1
            while k<l:
                total = nums[i]+nums[j]+nums[k]+nums[l]
                if total == target:
                    temp = [nums[i],nums[j],nums[k],nums[l]]
                    ans.append(temp)
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while l>k and nums[l]==nums[l+1]:
                        l-=1
                elif total>target:
                    l-=1
                elif total<target:
                    k+=1
    print(ans)
_4sum(nums)