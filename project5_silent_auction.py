import os

bidders = {}
flag = "yes"
while flag == "yes" :
    # os.system('cls')
    name = input("What is your name?")
    bid = int(input("what is your bid"))
    bidders[name] = bid
    flag = input("Are there any other bidders? Type (yes/no)").lower()

# find the bidders who bid the highest
maximum_bid = 0
bidder_name = ""
for bidder in bidders:
    value = bidders[bidder]
    if value > maximum_bid:
        bidder_name = bidder
        maximum_bid = value

print(f"The winner is {bidder_name} with {maximum_bid} bids.")