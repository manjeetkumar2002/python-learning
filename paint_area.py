import math
def paint_calculation(height,width,coverage_of_one_can) :
    area = height * width
    no_of_cans = math.ceil(area / coverage_of_one_can)
    return no_of_cans
h = int(input("Enter the height in meters :  "))
w = int(input("Enter the width int meters: "))
c = int(input("Enter the coverage of one cans : "))

result = paint_calculation(height=h,width=w,coverage_of_one_can=c)

print(f"You will need {result} cans to paint the whole wall")