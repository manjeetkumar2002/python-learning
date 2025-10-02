#program to calculate maximum number from a list of numbers
numbers=input("Enter a list of numbers separated by space : ")
numbers_list = numbers.split(" ")

for idx in range(len(numbers_list)):
    numbers_list[idx] = int(numbers_list[idx])

maximum_number = numbers_list[0]

for number in numbers_list:
    if number> maximum_number:
        maximum_number = number

print(f"The maximum number is: {maximum_number}")