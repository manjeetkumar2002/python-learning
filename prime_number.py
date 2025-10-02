#check a number is prime or not

#Approach1
# def isprime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

#Approach2
import math
def isprime(num):
    if num == 1:
        return False
    for i in range(2,math.ceil(num/2)+1):
        if num % i == 0:
            return False
    return True


number = int(input("Enter the number :  "))
result = isprime(number)
if result :
    print(f"{number} is prime")
else :
    print(f"{number} is not prime")