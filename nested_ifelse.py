height=int(input("enter your height : "))

if height>=3 :
    print("You can ride")
    age=int(input("enter your age : "))
    if age>=18 :
        print("please pay 500rs")
    else :
        print("please pay 200rs")
else:
    print("sorry! you cant ride")
print("Bye")