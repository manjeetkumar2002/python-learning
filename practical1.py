# Practical 1 :
# Write a Python program to create a list of ‘n’ integers and modify the list by replacing all 2-digit numbers with the sum of their digits.

def replace_two_digit_sum(lst):   #called function
    new_list = []
    for num in lst:
        if 10 <= num <= 99:   # check for 2-digit number
            s = 0
            temp = num
            while temp > 0:
                s += temp % 10
                temp //= 10
            new_list.append(s)
        else:
            new_list.append(num)
    return new_list

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

modified_list = replace_two_digit_sum(lst)  #called Function

print("Original List:", lst)
print("Modified List:", modified_list)

