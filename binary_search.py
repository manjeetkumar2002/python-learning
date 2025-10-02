numbers = input("Enter a list of numbers separated by space: ")
numbers_list = numbers.split(" ")
key = int(input("Enter the key you want to search for: "))

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

found = False
start = 0
end = len(numbers_list)-1

while start <= end :
    mid = start + (end - start)//2
    if numbers_list[mid] == key:
        found = True
        break
    elif key<numbers_list[mid]:
        end = mid-1
    else:
        start = mid+1

if not found:
    print("Key not found")
else :
    print("Key found")