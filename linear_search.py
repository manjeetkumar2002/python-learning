numbers = input("Enter a list of numbers separated by space: ")
numbers_list = numbers.split(" ")
key = int(input("Enter the key you want to search for: "))

for idx in range(len(numbers_list)):
    numbers_list[idx] = int(numbers_list[idx])

found = False
for num in numbers_list:
    if num == key:
        print(f"{num} was found")
        found = True
        break

if not found:
    print("Key not found")