def armstrong_number(n):
    num = n
    nod = len(str(n)) #number of digits
    total = 0
    while num > 0:
        total += (num % 10)**nod
        num = num // 10

    if total == n:
        print("Number is Armstrong")
    else :
        print("Number is not Armstrong")

number = int(input("Enter a number: "))
armstrong_number(number)