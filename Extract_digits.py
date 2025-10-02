# Extract Digits from a number

def extract_digits(n):
    num = n
    while num>0 :
        last_digit = num % 10
        print(last_digit,end=" ")
        num = num // 10

extract_digits(123456)