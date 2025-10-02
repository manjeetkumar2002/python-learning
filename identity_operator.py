# identity operator used for comparing objects
#  types => is , is not

# in python ,agar variables me same data h , to memory manager ussi same data ko use karta h new create nhi karta
# it means a and b pointing to same data
# identity operator checking the locations of variables
# == operator check the values not the addresses of variable
a = 5
b = 5
print(a is b) # true because both the objects are same pointing to same locations

# id() return the address of a variable
print(id(a))
print(id(b))


str  = '5'
num = 5

print(str is num) # false because both are different objects both have different address

# is not operator is just opposite of is

print(str is not num)

print(a is not b)

print(a==b) # it is checking the value

str1 = "banana shake"
str2 = "banana shake"
print(str1 is str2) # true both sharing the same locations

str3 = "mango shake"
print(id(str1) == id(str2)) # true here we are comparing the values of address which are same
print(id(str1) == id(str3)) # false here we are comparing the values of address which are different