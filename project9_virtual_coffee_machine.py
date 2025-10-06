import os
Menu = {
    "latte":{
        "ingredients":{
            "water":100,
            "coffee":200,
            "milk":300,
        },
        "cost":150
    },
    "espresso":{
        "ingredients":{
            "water":70,
            "coffee":100,
            "milk":100,
        },
        "cost":200
    },
    "cappuccino":{
        "ingredients":{
            "water":70,
            "coffee":100,
            "milk":100,
        },
        "cost":200
    }
}
profit = 0
resource = {
    "water":1000,
    "coffee":300,
    "milk":400,
}
def check_sufficient_resource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resource[item]:
            print(f"Sorry, we don't have enough {item}")
            return False
    return True

def process_coins():
    total = 0
    coins_five = int(input("How many 5 coins? "))
    coins_ten = int(input("How many 10 coins? "))
    coins_twenty = int(input("How many 20 coins? "))
    total = coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def is_payment_successful(amount, coffee_cost):
    if amount >= coffee_cost:
        global profit
        profit+=coffee_cost
        change = amount - coffee_cost
        print(f"here is your change: {change}")
        return True
    else :
        print("Sorry, you added less amount")
        return False

def make_coffee(coffee_name,order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]

    print(f"Here is your {coffee_name}... enjoy!!!")

is_on = True
while is_on:
    os.system('cls')
    choice = input("what would you like to have ? (latte/espresso/cappuccino) : ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water = {resource['water']} ml")
        print(f"milk = {resource['milk']} ml")
        print(f"coffee = {resource['coffee']} gm")
    else :
        coffee_type = ""
        if choice in Menu:
            coffee_type = Menu[choice]
        else:
            print("Invalid choice")
        print(coffee_type)

        if check_sufficient_resource(coffee_type["ingredients"]) :
            payment = process_coins()
            if is_payment_successful(payment, coffee_type["cost"]):
                make_coffee(choice,coffee_type["ingredients"])


