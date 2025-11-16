import random

#TODO-1 
# Randomly choose a word from the word_list and assign it to a variable called `chosen_word`. Then print it.
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
chosen_word = word_list[random.choice(range(len(word_list)))]     # Select a random word from the list, random.choice from range which is int, so use len()
print(chosen_word) 


###TODO-2 
# Ask the user to guess a letter and assign their answer to a variable called `guess`. Make the String stored in `guess` lowercase

guess = input("Guess a letter: ").lower()
print(guess)



# TODO-3 
# Check if the letter the user guessed `guess` is one of the letters in the `chosen_word`. Loop through each of the letters in the `chosen_word`  and print "Right" if the letter is a match, "Wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("Correct")
    else:
        print("Wrong")