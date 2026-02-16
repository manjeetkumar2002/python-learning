# 3. Write a python program to check Armstrong numbers for both 3-digit and 4-digit numbers
#
# What is an Armstrong Number?
# A number is an Armstrong number if the sum of each digit raised to the power of number of digits equals the number itself.
#
# Examples:
# •	3-digit: 153 = 1³ + 5³ + 3³ ✅
# •	4-digit: 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴ ✅



def is_armstrong(num):
    digits = len(str(num))
    temp = num
    s = 0

    while temp > 0:
        d = temp % 10
        s += d ** digits
        temp //= 10

    return s == num


num = int(input("Enter a number: "))

if (100 <= num <= 999) or (1000 <= num <= 9999):
    if is_armstrong(num):
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
else:
    print("Please enter only 3-digit or 4-digit number")


