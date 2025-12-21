list = [1,2,3]
result = []
def solve(index,subset):
    if index >= len(list):
        result.append(subset.copy())
        return

    # take the element
    subset.append(list[index])
    solve(index+1,subset)
    # don't take the element
    subset.pop()
    solve(index+1,subset)

solve(0,[])

for i in result:
    print(i)
