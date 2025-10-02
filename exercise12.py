import random
names = input("Enter everybody's name separated by comma: ")
names_list = names.split(',')
print(names_list)

#rand_index = random.randint(0,len(names_list)-1)
rand_index = random.randrange(0, len(names_list))
print(f"{names_list[rand_index]} will pay the bill")