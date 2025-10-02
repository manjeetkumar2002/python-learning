# Approach1 :Brute Force
# def factors(number):
#     n = number
#     result = []
#
#     for divisor in range(1,n+1):
#         if n % divisor == 0:
#             result.append(divisor)
#
#     return result

#Apprach2 : Better than brute force
# def factors(number):
#     n = number
#     result = []
#
#     for divisor in range(1,n//2+1):
#         if n % divisor == 0:
#             result.append(divisor)
#     result.append(n)
#     return result


#Apprach3 : optimal solution
import math
def factors(number):
    n = number
    result = []

    for divisor in range(1,int(math.sqrt(n))+1):
        if n % divisor == 0:
            result.append(divisor)
            if n // divisor != divisor:
                result.append(n//divisor)
    result.sort()
    return result

number = int(input("Enter a number: "))
res = factors(number)
print(res)