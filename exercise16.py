#calculate sum of even numbers from 1 to 100 ,including 1 & 100

# sum = 0
# for number in range(1,101) :
#     if number % 2 == 0 :
#         sum += number
# print(f"The sum is: {sum}")

sum = 0
for number in range(2,101,2) :
    sum += number
print(f"The sum is: {sum}")