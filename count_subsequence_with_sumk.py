list = [5,4,2,3,1,9,7]
target = 9
count = 0
result = []
def solve(index,total,subset):
    if total == target:
        result.append(subset.copy())
        global count
        count += 1
        return
    if total > target:
        return
    if index >= len(list):
        return

    # Include the element
    sum = total + list[index]
    subset.append(list[index])
    solve(index+1,sum,subset)
    # Exclude the element
    subset.pop()
    sum = total
    solve(index+1,sum,subset)

solve(0,0,[])
print(f'Total subsequence: {count} with sum: {target}')
print(f"Subsequence: {result}")