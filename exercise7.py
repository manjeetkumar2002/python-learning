weight = input("enter your weight in kg : ")
height = input("enter your height in m  : ")
BMI = round(int(weight) / (float(height) ** 2),2) #let's round it to 2 decimal places

print("Your BMI is:", BMI)
if BMI < 16.0:
    print("you are under weight(severe thickness)")
elif BMI <= 16.9:
    print("you are under weight(moderate thickness)")
elif BMI <= 18.4:
    print("you are under weight(mild thickness)")
elif BMI <= 24.9:
    print("you are in normal range")
elif  BMI <= 29.9:
    print("you are overweight(pre-obese)")
elif  BMI <= 34.9:
    print("you are obese(class1)")
elif BMI <= 39.9:
    print("you are obese(class2)")
elif BMI>=40.0 :
    print("you are obese(class3)")

