# variables are container for storing values
name = input("what is your name? ")
print("your name is "+name)
length = len(name) # len() function is used to calculate the length of a string
print("Length is "+str(length)) # we have to typecast the length because we can't concatenate integer with string , so we need to convert length into string