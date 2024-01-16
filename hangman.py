# normal hangman game

import random
from art import stages

word_list = ["pillow", "banana", "people", "principle", "president", "minister", "religion"]

# creating code:

selected_word = random.choice(word_list)
print(selected_word)

letter_in_word = []
for letter in selected_word:
    letter_in_word.append("_")
print(letter_in_word)

attempt = 6
while attempt > 0 and "_" in letter_in_word:

    user_input = input("\nguess the letter: ").lower()

    if user_input in selected_word:
        if user_input not in letter_in_word:
            for i in range(len(selected_word)):
                if user_input == selected_word[i]:
                    letter_in_word[i] = user_input

            print(letter_in_word)
            print(f"you've {attempt} lives left.")

            if "_" not in letter_in_word:
                print("\nYOU WON.")
                print(f"The letter was: {selected_word}")

        else:
            print("you've already guessed the letter. Guess new letter.\n")
            # continue

    else:
        attempt -= 1
        print(letter_in_word)
        print(f"you've {attempt} lives left.")
        if attempt == 0:
            print("you lose")
            print(f"The letter was: {selected_word}")

    print(stages[attempt])



