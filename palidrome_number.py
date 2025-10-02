def reverse(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //=10
    return reversed_num

def palindrome_number(num) :
    return reverse(num) == num

number = int(input("Enter a number: "))
result = palindrome_number(number)

if result:
    print("Number is Palindrome")
else :
    print("Number is not Palindrome")