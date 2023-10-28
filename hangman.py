import random
from hangman_ascii import logo, stages
from hangman_wordlist import word_list

end_of_game = False
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
lives = 6

display = []

for character in chosen_word:
    display.append("_")

print(logo)

while not end_of_game:
    guess = input("Guess a letter:  ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for postition in range(chosen_word_length):
        letter = chosen_word[postition]
        if letter == guess:
            display[postition] = letter
    if guess != chosen_word:
        lives = lives -1
        print(stages[lives])
        if lives == 0:
            print("Game Over")
            break
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")