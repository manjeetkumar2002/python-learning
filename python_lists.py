numbers = [1,53,66,5,67]
print(numbers)
print(type(numbers))
print(numbers[1])


names = ["manjeet","amit"]
print(names)

mix_list = ["aman",32,True,3,5,6]
print(mix_list)

print(len(mix_list))

# negative index also valid

print(mix_list[-1]) # point to last element

# list slicing

# print complete list
print(mix_list[0:3])
print(mix_list[0:])
print(mix_list[:])
#print a part of list
print(mix_list[1:3]) #3 is excluded

nums = [1,2,3]
print(nums[0:3:2]) # third value represent jumps between element here 2 means one element is skipped


arr =[3,45,1,5,6]
# sort in ascending order

# we can't apply sorting on mix list
arr.sort()
print(arr)
arr.reverse()
print(arr)
print(min(arr)) # return minimum element
print(max(arr)) # return maximum element

# insert new element at the end

arr.append(3553)
print(arr)


# insert at a particular index
arr.insert(0,1090)

print(arr)

# add multiple elements in the list at the end

arr.extend([1,2,3])
print(arr)

# modifying single element at a index

arr1 = [1,2,3,4,5,6,7]

arr1[1] = 34
print(arr1)

arr1[1:4] = [44,45,46] # it will modify element from index 1 to 4
print(arr1)


# how to remove first occurrence of a element

arr2 = [1,2,3,4,5,6,7,2]
arr2.remove(2)
print(arr2)

num=arr2.pop() # it removes and return the last element
print(num)

# remove from a particular index
print(arr2.pop(1))