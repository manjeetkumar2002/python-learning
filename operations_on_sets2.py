#1 isdisjoint() : if there is nothing common in two sets then they are disjoint sets


set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7,8}
print(set1.isdisjoint(set2)) # false because 3,4,5 are common

set1 = {1,2}
set2 = {3,4,5,6,7,8}
print(set1.isdisjoint(set2)) # true because nothing is common

#2 issubset() : check a set is subset of another set
# set2 is subset of set1 if set1 contains all the elements of set2

set1 = {1,2,3,4,5}
set2 = {3,4}

print(set2.issubset(set1)) # true
print(set1.issubset(set2)) # false
#3 issuperset : set1 is superset of set2 when set1 contain every elements of set2

set1 = {1,2,3,4,5}
set2 = {3,4,5}
print(set1.issuperset(set2)) # true


#4 clear() : erase all the elements of set but don't delete the set
set1 = {1,2,3,4,5}
set1.clear()
print(set1)

#5 del : it erase the set and also delete the set

set1 = {1,2,3,4,5}

del set1
#print(set1) #NameError: name 'set1' is not defined. Did you mean: 'set2'?