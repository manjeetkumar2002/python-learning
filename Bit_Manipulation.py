def convert2Binary(num):
    result = ''
    while num > 0:
        if num % 2 == 0:
            result += '0'
        else:
            result += '1'
        num//=2
    result = result[::-1]
    return result

num = int(input('Enter a number: '))
print(f"Binary conversion of {num} is {convert2Binary(num)}")

def convert2Decimal(str):
    decimal_number = 0
    index = len(str) - 1
    power = 0
    while index >= 0:
        decimal_number += int(str[index]) * (2 ** power)
        index -= 1
        power += 1

    return decimal_number

print(f"Decimal conversion of {10001} is {convert2Decimal('10001')}")