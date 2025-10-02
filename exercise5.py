current_age = input("Enter your current age: ")
remaining_years = 90-int(current_age)
print(remaining_years)

days = remaining_years*365
months = remaining_years*12
weeks = remaining_years*52

print(F"you have {days} days, {months} months, {weeks} weeks left")