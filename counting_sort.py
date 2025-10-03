numbers = input("Enter a list of numbers separated by space in range (1 to N): ")
numbers_list = numbers.split(" ")

for idx in range(len(numbers_list)):
    numbers_list[idx] = int(numbers_list[idx])

list_length = len(numbers_list)

i = 0
while i < list_length:
    correct_index = numbers_list[i] - 1
    if numbers_list[i] != numbers_list[correct_index]:
        numbers_list[i],numbers_list[correct_index] = numbers_list[correct_index],numbers_list[i]
    else :
        i += 1

print(numbers_list)