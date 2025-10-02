import random

print("Let me think of a number between 1 and 50")
comp_guess = random.randint(1, 50)
difficult = input("Choose level of difficult ...type 'easy' or 'hard' :").lower()
if difficult == 'easy':
    total_attempts = 10
else :
    total_attempts = 5

while total_attempts > 0:
    print(f"You have {total_attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess : "))
    if user_guess == comp_guess:
        print(f"You guessed the number {user_guess}!")
        break
    elif user_guess > comp_guess:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    print("Guess again.")
    total_attempts = total_attempts - 1

if total_attempts == 0:
    print("Sorry, you ran out of guesses.")
print("Thank you for playing!")