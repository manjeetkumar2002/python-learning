# nums contain element in range 0 to N , except one element is missing

nums = [9,6,4,2,3,5,7,0,1]

# APPROACH1 : CHECK EACH ELEMENT FROM 0 TO N PRESENT OR NOT IN THE LIST
# def missing_element(nums):
#     n = len(nums)
#     for num in range(0,n+1):
#         if num not in nums:
#             print("missing element = ",num)
#             return

# APPROACH2: STORE FREQUENCY OF EACH ELEMENT FROM 0 TO N IN DICTIONARY,THEN CHECK IF ELEMENT IN DICT HAVE FREQUENCY 0 THEN IT IS MISSING
# def missing_element(nums):
#     n = len(nums)
#     freq_dict = dict()
#     for i in range(0,n+1):
#         freq_dict[i] = 0
#
#     for i in range(0,n):
#         freq_dict[nums[i]] = 1
#
#     for key,value in freq_dict.items():
#         if value == 0:
#             print("missing element = ",key)
#             return

# APPROACH3 : FIND THE SUM OF 0 TO N ELEMENT AND ALSO FIND THE SUM OF ELEMENT OF LIST , RETURN THE DIFFERENCE

def missing_element(nums):
    n = len(nums)
    SUM = n*(n+1)/2
    LIST_SUM = sum(nums)
    missing_number = SUM - LIST_SUM
    print("missing element = ",missing_number)
missing_element(nums)