# how to create tuple

tuple1 = (1,2,-1,"amit",True)
print(tuple1)
tuple2 = (1,) # if tuple have only one value add comma after that value ,otherwise it is not a tuple
print(tuple2)
tuple3 = (1) # this is not a tuple it is a variable having integer value
print(tuple3)
print(type(tuple3)) # output : <class 'int'>


# we can access tuples element same as list with brackets []

print(tuple1[3])
print(tuple1[-1]) # negative indexing also possible
print(type(tuple1)) # output : <class 'tuple'>

# Note : tuples are immutable and list are mutable
# we can't change the data of tuple

# tuple1[1] = "manjeet"
# print(tuple1)

# Duplicate items are also allowed

# slicing also possible in tuple
print(tuple1[1:])
print(tuple1[3:len(tuple1)-1])

print(tuple1[0::2]) # third value is for steps,how many steps you want to skips

# Nesting of tuples also possible

t1 = (1,2,3)
t2 = (4,5,6)
t3 = (t1,t2)
print(t3)

print(t3[0])
print(t3[1])

print(t3[1][2])
print(len(t3))

# concatenating tuples
t4 = t1 + t2
print(t4)
print(len(t4))
# min max not work if tuple is of mixed type
print(min(t4))
print(max(t4))
print(t4.count(1))
print(t4.index(4))


# we can convert a list into tuple

l1 = [1,2,3,4,5,6]
print(tuple(l1))


t6 = ("jenny",) *5
print(t6)