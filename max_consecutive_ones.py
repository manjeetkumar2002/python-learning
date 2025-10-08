nums = [1,1,0,1,0,1,1,1,1,0,1,1]

def func(nums):
    count = 0
    result = float("-inf")
    for num in nums:
        if num == 1:
            count += 1
        else :
            result = max(result, count)
            count = 0
    return result

print(func(nums))
