import random

options = ["rock", "paper", "scissors"]

userChoice = input('Enter your choice (rock, paper, scissors): ').lower()

# Validate user input
if userChoice not in options:
    print("Invalid choice. Please choose rock, paper, or scissors.")
    exit()

rand_idx = random.randint(0, len(options) - 1)
computerChoice = options[rand_idx]

print(f"Computer chose: {computerChoice}")

if userChoice == computerChoice:
    print('Draw')
elif userChoice == "rock" and computerChoice == "paper":
    print('You lose, paper covers rock')
elif userChoice == "rock" and computerChoice == "scissors":
    print('You win, rock smashes scissors')
elif userChoice == "scissors" and computerChoice == "rock":
    print('You lose, rock smashes scissors')
elif userChoice == "scissors" and computerChoice == "paper":
    print('You win, scissors cut paper')
elif userChoice == "paper" and computerChoice == "scissors":
    print('You lose, scissors cut paper')
elif userChoice == "paper" and computerChoice == "rock":
    print('You win, paper covers rock')