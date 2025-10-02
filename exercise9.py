pizza_size = input("what size pizza do you want (small,medium,large)?")

bill = 0

if pizza_size == "small":
    bill = bill + 100
elif pizza_size == "medium":
    bill = bill + 200
else :
    bill = bill + 300

add_pepperoni=input("Do you want to add pepperoni in the pizza? (Y,N) : ")


if add_pepperoni == "Y" or add_pepperoni == "y":
    if pizza_size == "small":
        bill = bill + 30
    else: 
        bill = bill + 50

add_cheese = input("Do you want to add cheese in the pizza? (Y,N) : ")

if add_cheese == "Y" or add_cheese == "y" :
    bill = bill + 20

print(F"Your bill is {bill} for {pizza_size} pizza")
