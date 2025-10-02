set1 = {1,True,"jenny",1.2445}
print(set1)
# print(set1[3]) TypeError: 'set' object is not subscriptable


set2 = {} # this is not the way to create empty set it create dict
print(set2)
print(type(set1)) #<class 'set'>
print(type(set2)) #<class 'dict'>

#right way to create empty set
set3 = set()
print(set3)
print(type(set3))

set4 = set()
set4.add("manjeet")
set4.add("amit")
print(set4)
print(len(set4))

set4.remove("amit")
print(set4)
# if element is not present that you are trying to remove it gave keyError
set4.discard("karan") # discord not gave keyError if not present , if present it remove that element
print(set4)

set4.clear() # remove all the elements
print(set4)

item = set1.pop() # it removes a random element and also return that element
print(item)

set5 = set()
set5.add((1,2,3)) # you can also add any immutable item eg tuple
print(set5)

set6 = {(1,2,4)}
print(set6)

# cant possible to add a list in set
# set7 = {[1,2,4]}