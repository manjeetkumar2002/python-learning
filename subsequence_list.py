list = [1,2,3]
result = []
def solve(index,subset):
    if index >= len(list):
        result.append(subset.copy())
        return

    # Include the element
    subset.append(list[index])
    solve(index+1,subset)
    # Exclude the element
    subset.pop()
    solve(index+1,subset)

solve(0,[])

for i in result:
    print(i)
