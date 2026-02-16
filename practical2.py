# Practical 2:
# A. To create a dictionary named Stock which consists of the details of ‘n’ number of products including product_id as key and pname, price, qty, brandname as a list of values. Display the dictionary.
# B. Write a code to increase the price of a certain product based on the product id entered. If the product id is found, update the price; otherwise print the message:



def create_stock(n): 		#Called Function with 1 parameter
    stock = {}

    for i in range(n):
        pid = input("Enter Product ID: ")
        pname = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        qty = int(input("Enter Quantity: "))
        brand = input("Enter Brand Name: ")

        stock[pid] = [pname, price, qty, brand]

    return stock

n = int(input("Enter number of products: "))
stock = create_stock(n)   #Calling function

print("\nStock Details:")
for pid, details in stock.items():	#for loop using .items()
    print(pid, ":", details)
