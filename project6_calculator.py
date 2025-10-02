import os

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operations_dict = {
    '+': add,
    '-': sub,
    '*': mul,
    '/':div
}

def calculator():

    number1 = int(input("Enter first number: "))
    # printing the operations symbols
    for symbol in operations_dict:
        print(symbol)

    flag = True
    while flag:
        op_symbol = input("Pick an operation:")
        number2 = int(input("Enter second number: "))
        calculator_function = operations_dict[op_symbol]
        output = calculator_function(number1, number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        should_continue = input(
            f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x to exit :").lower()
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            #use recursion here
            flag = False
            os.system('cls')
            calculator()
        elif should_continue == 'x':
            flag = False
            print("Bye")

calculator()

