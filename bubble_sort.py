numbers = input("Enter a list of numbers separated by space: ")
numbers_list = numbers.split(" ")

for idx in range(len(numbers_list)):
    numbers_list[idx] = int(numbers_list[idx])

list_length = len(numbers_list)

for i in range(list_length-1):
    for j in range(0,list_length-i-1):
        if numbers_list[j] > numbers_list[j+1]:
            numbers_list[j],numbers_list[j+1] = numbers_list[j+1],numbers_list[j] # swapping

print(numbers_list)
