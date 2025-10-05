def is_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4, 5]))