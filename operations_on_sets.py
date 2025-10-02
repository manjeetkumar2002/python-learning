set1 = {"Ram","Shyam","Jenny"}
set2 = {"Jenny","Jiya","Akash"}
print(set1.union(set2)) # output : {'Shyam', 'Jenny', 'Ram', 'Akash', 'Jiya'}
print(set1 | set2)

print(set1.intersection(set2)) # output : {'Jenny'}
print(set1 & set2)


set3 = {1,2,3}
set4 = {1,2,3,4,5}
# update join the sets and update the set3
# set3.update(set4)
# print(set3)

#method2 =>join and update the set3
set3|=set4
print(set3)

set5 = {1,2,3,4,5}
set6 = {1,2,3,4,5,6,7,8,9}

set5.intersection_update(set6)
print(set5)
