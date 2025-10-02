numbers = input("Enter a list of numbers separated by space: ")
numbers_list = numbers.split(" ")

for idx in range(len(numbers_list)):
    numbers_list[idx] = int(numbers_list[idx])

list_length = len(numbers_list)

for i in range(list_length-1):
    for j in range(i+1,list_length):
        if numbers_list[i] > numbers_list[j]:
            numbers_list[i],numbers_list[j] = numbers_list[j],numbers_list[i] # swapping

print(numbers_list)
