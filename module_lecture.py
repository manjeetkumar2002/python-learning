# print(help("modules")) # print all inbuild modules present in python
# print(help("random")) # print all function available in random module
# print(help("math")) # print all function available in math module
import math
print(math.pi)


# importing user defined modules
import my_module

# if name of module is large name then use alias
# import my_module as m

# if you have a lots of function in modules , and you want to import only one function
from my_module import area_of_square
# from my_module import area_of_square ,area_of_circle
# from my_module import * => import all the things
# you can use alias in it also
# from my_module import area_of_square as area
print(my_module.area_of_circle(21))
print(my_module.area_of_rectangle(21, 20))
print(my_module.a)

print(area_of_square(100))