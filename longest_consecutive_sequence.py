nums = [1,99,101,98,2,5,3,99,100,1,1]

#BRUTE FORCE
def longest_consecutive_sequence(nums):
    n = len(nums)
    max_count = 0
    for i in range(n):
        num = nums[i]
        count = 1
        while num+1 in nums:
            count += 1
            num +=1
        max_count = max(max_count, count)
    print(f"longest consecutive sequence length is : {max_count}")


#BETTER SOLUTION
def longest_consecutive_sequence2(nums):
    n = len(nums)
    nums.sort()
    count = 0
    longest = 0
    last_smallest = float('-inf')
    for i in range(0,n):
        num = nums[i]
        if num - 1 == last_smallest:
            count += 1
            last_smallest = num
        elif num!=last_smallest:
            count = 1
            last_smallest = num
        longest = max(count, longest)
    print(f"longest consecutive sequence length is : {longest}")

# longest_consecutive_sequence2(nums)

# OPTIMAL SOLUTION

def longest_consecutive_sequence3(nums):
    n = len(nums)
    my_set = set()
    longest = 0
    for num in nums:
        my_set.add(num)

    for num in my_set:
        # if num-1 not in my_set it means we get a sequence starting point
        if num-1 not in my_set:
            x = num
            count = 1
            # calculate the length of this sequence
            while x+1 in my_set:
                count += 1
                x = x + 1
            longest = max(count, longest)
    print(f"longest consecutive sequence length is : {longest}")

longest_consecutive_sequence3(nums)