def reverse(nums,left,right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    reverse(nums,left+1,right-1)

number = input("Enter a list of numbers separated by space: ")
numbers_list = number.split(" ")
reverse(nums = numbers_list,left = 0,right = len(numbers_list)-1)
print("reverse array : ",numbers_list)