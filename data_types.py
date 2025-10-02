# In python data type are classes and this variable are the instance
a = 123  #int
b = 3.14 #float
c = True #boolean
name = "Manjeet" #string
# NOTE :- There is not range limit in int ,float

# type() is function use for checking the type of the variable
print(type(a))
print(type(b))
print(type(c))
print(type(name))


# OUTPUT
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'str'>

#print hello world 5time
print(5*"hello world!")

# OUTPUT
# hello world!hello world!hello world!hello world!hello world!

# USE OF BACKSLASH FOR SKIPING THE SPECIAL MEANING OF CHARCTER
print("Hello \"Manjeet\" ,\nHow are your?") # here we skip the meaning of double quotes


# prefix : Ox ,OX ,Oo ,OO, Ob ,OB
# x is for hexadecimal
# o is for octal
# b is for binary

octal1 = 0o123
octal2 = 0O123
print(octal1) #83
print(octal2) #83

hexadecimal1 = 0x123
hexadecimal2 = 0x123
print(hexadecimal1)
print(hexadecimal2)

binary1 = 0b011
binary2 = 0b01
print(binary1)
print(binary2)
