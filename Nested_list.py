l = [1,2,3,[5,6,7],23,54]

print(l)

print(l[3])

print(l[3][1])

print(len(l)) # len is 6 not 8

#sliced_list = l[3][:]
sliced_list = l[3][0:3] 

print(sliced_list)