nums = [2,3,5,6,7,1]
def largest_element(arr):
    n = len(arr)
    if n == 0:
        return float('-inf')
    largest = arr[0]
    for i in range(1,n):
        largest = max(largest,arr[i])
    return largest

print(largest_element(nums))