import random


# Randomly choose a word from the word_list and assign it to a variable called `chosen_word`. Then print it.
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
chosen_word = random.choice (word_list)    # Select a random word from the list, random.choice from range which is int, so use len()
print(chosen_word)  # For testing purposes


# Ask the user to guess a letter and assign their answer to a variable called `guess`. Make the String stored in `guess` lowercase
guess = input("Guess a letter: ").lower()




# - Create an empty String called `placeholder`.
# - For each letter in the chosen_word, add a `_` to `placeholder`.
# - So if the `chosen_word` was "apple", `placeholder` should be `_ _ _ _ _` with 5 `"_"` representing each letter to guess.
# - Print out `hint`.


placeholder = ""
word_length = len(chosen_word)
for letter in range(word_length):
    placeholder += " _"
print(placeholder)




# False_Get the user guess again as long as the guess is not correct, till we get the end of the script
# key_character = list(chosen_word)               # Convert the chosen word into a list of characters
# while guess != key_character:
#     guess = input("Guess a letter: ").lower()
#     break


game_over = False
correct_letters = []            #list to store correct guessed letters. list accumulates while the loop runs


while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)                    #add correct guessed letter to the list
        elif letter in correct_letters:                        #if the letter is already guessed correctly in previous while loop before, de lan doan tiep theo blank dan dan dc fill
            display += letter
        else:
            display += "_"

    print(display)


    if "_" not in display:                      #there is no more blanks, all letters are guessed
        game_over = True
        print("You win")
