import random
from hangman_words import word_list       #alternative: only "import word_list", but use from in case in hangman_words have multiple lists/variables/functions
from the_hangman_art import stages
from the_hangman_art import logo 


#Create a variable called `lives` to keep track of the number of lives left. start with 6 lives
lives = 6            



#Print game logo
print(logo)

# Select a random word from the list, random.choice from range which is int, so use word_list directly
chosen_word = random.choice (word_list)    
print(chosen_word)      #for testing purposes


# - Create an empty String called `placeholder`.For each letter in the chosen_word, add a `_` to `placeholder`. So if the `chosen_word` was "apple", `placeholder` should be `_ _ _ _ _` with 5 `"_"` representing each letter to guess.
# - Print out `hint`.
placeholder = ""
word_length = len(chosen_word)
for letter in range(word_length):
    placeholder += " _"
print(placeholder)






# Define group: correct letters = display to store correct guessed letters; guess_letter = set() to store all guessed letters, including wrong & correct ones; wrong_guesses = set() to store wrong letters


# Create a set to store all guessed letters
guessed_letter = set()       #we need set (not list) to avoid duplicated guessed letters
wrong_guesses = set()   # empty set to store wrong letters, so we don't lose lives for repeated wrong guess, just warn user



# Get the user guess again as long as the guess is not correct, till we get the end of the script

while True:          #True means loop will run until we break it, alternative: "game_over = False, while not game_over:"
    
    
    # rebuild and show the display string based on guessed letters. Check if the letter the user guessed `guess` is one of the letters in the `chosen_word`. Loop through each of the letters in the `chosen_word`
    display = ""
    for letter in chosen_word:              #condition for correct guess to display
        if letter in guessed_letter:     
            display += letter
            print ("Good guess!")                 ##if guessed letter is correct, add it to display 
        else:
            display += "_"
    print(display)



    #win condition: if every letter in chosen_word is guessed, stop the loop
    if all(letter in guessed_letter for letter in chosen_word):    #all() returns True if all letters in chosen_word are in guessed_letter set
        print("Congratulations! You've guessed the word:", chosen_word)
        break
    else:               #when not all letters are guessed, ask for another letter
        guess = input("Guess a letter: ").lower()


    # ignore repeated guesses
    if guess in display or guess in wrong_guesses:       # if guess was displayed before (correct) or wrongly made. 
        print("You've already guessed that letter. Try again.")
        continue
    
    
    #correct guess: add correct guessed letter to the guessed_letter set
    if guess in chosen_word:
        print("Good guess!")
        guessed_letter.add(guess)        
    
    
    #wrong guess: if guess is not in chosen_word, reduce lives by 1
    else:
        wrong_guesses.add(guess)      #add wrong guessed letter to the wrong_guesses set
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. {lives} LIVES LEFT!!!")
        print(stages[lives])                   #print the ASCII art from the list `stages` that corresponds to the current number of `lives` the user has remaining.
        if lives == 0:
            print("You lose. The word was:", chosen_word)
            break

                     
  