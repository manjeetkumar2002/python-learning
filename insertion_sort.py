numbers = input("Enter a list of numbers separated by space: ")
numbers_list = numbers.split(" ")

for idx in range(len(numbers_list)):
    numbers_list[idx] = int(numbers_list[idx])

list_length = len(numbers_list)

for i in range(1,list_length-1):
    item =  numbers_list[i]
    j = i - 1
    while j>=0 and numbers_list[j] > item :
        numbers_list[j+1] = numbers_list[j]
        j = j - 1
    numbers_list[j+1] = item

print(numbers_list)
