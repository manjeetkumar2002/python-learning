nums = [2,3,4,5,6]
target = 7

def solve(index,total,subset,result,target):
    if total == target:
        result.append(subset.copy())
        return
    if total > target:
        return
    if index >= len(nums):
        return

    subset.append(nums[index])
    sum = total + nums[index]
    # pick the same element
    solve(index,sum,subset,result,target)
    # not pick this element
    sum = total
    subset.pop()
    solve(index+1,sum,subset,result,target)


def combinations_sum(nums, target):
    result = []
    solve(0,0,[],result,target)
    return result


print(combinations_sum(nums,target))


