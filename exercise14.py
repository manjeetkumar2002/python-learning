#program to calculate average height from a list of heights
heights = input("enter all heights separated by space : ")
height_list = heights.split(" ")

# finding the length of height_list manually
count = 0
for i in height_list:
    count += 1

# convert each item into int
# range function generate value 0 to count
for idx in range(0,count) :
    height_list[idx] = int(height_list[idx])

total = 0
for i in height_list:
    total+=i

avg = total/count
print(f"Average height is {round(avg)}")
