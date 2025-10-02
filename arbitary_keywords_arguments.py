
# def info_person(**person): # kwargs is a dictionary not a tuple
#     print(person)
#     print(f"Name : {person['name']}")
#     print(f"Age : {person['age']}")
#
# info_person(name="jenny",age=20)


# def info_person(*args,**person):
#     print(args)
#     print(person)
#
# info_person(1,2,3,4,name="jenny",age=20,tel="123")


def info_person(balance,acc,*args,**person):
    print(f"balance is {balance}")
    print(f"account number is {acc}")
    print(args)
    print(person)

info_person(12,34,1,2,3,4,name="jenny",age=20,tel="123")