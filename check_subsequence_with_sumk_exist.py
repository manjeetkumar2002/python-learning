list = [5,4,2,3,1,9,7]
target = 5
def solve(index,total):
    if total == target:
        return True
    if total > target:
        return False
    if index >= len(list):
        return False

    # Include the element
    sum = total + list[index]
    pick = solve(index+1,sum)
    if pick == True:
        return True
    # Exclude the element
    sum = total
    not_pick = solve(index+1,sum)
    return not_pick

print(solve(0,0))

