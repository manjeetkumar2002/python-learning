def add(*nums,name): #nums is a tuple
    # print(type(nums))
    # You cant modify a tuple
    print(name)
    Sum = 0
    for num in nums:
        Sum += num
    print(f"Sum is : {Sum}")

add(1,2,3,name="jenny")
# add(3,4,5,5,6,7)
# add(3,3,4)


def mul(*numbers):
    res = 1
    for num in numbers:
        res *=num
    print(f"Res is : {res}")

mul(1,2,3,4)
mul(1,2,3,4,5)