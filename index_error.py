# Index Error occur when you try to access a element of a list which is out of range

arr = [1,2,3,4,5]
size = len(arr)

print(arr[size-1])
print(arr[size]) # IndexError: list index out of range
