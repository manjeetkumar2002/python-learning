import random
import hangman_stages
import word_file
chosen_word = random.choice(word_file.words)
display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)
lives = 5
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guessed_letter:
            display[i] = letter
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")
    if "_" not in display:
        game_over = True
        print("You win!")
    print(display)
    print(hangman_stages.stages[lives])