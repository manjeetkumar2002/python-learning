import math

#Approach 1
# def count_digits(n):
#     return int(math.log10(n)+1)

#Approach 2
def count_digits(n):
    num = n
    count = 0
    while num>0:
        count+=1
        num//=10
    return count


number = int(input("Enter the number :  "))
print(f"The number of digits in {number} is {count_digits((number))}")