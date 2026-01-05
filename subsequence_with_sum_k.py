list = [5,4,2,3,1,9,7]
result = []
target = 9
def solve(index,total,subset):
    if total == target:
        result.append(subset.copy())
        return
    if total > target:
        return
    if index >= len(list):
        return

    # Include the element
    subset.append(list[index])
    sum = total + list[index]
    solve(index+1,sum,subset)
    # Exclude the element
    e=subset.pop()
    sum = total
    solve(index+1,sum,subset)

solve(0,0,[])

for i in result:
    print(i)
