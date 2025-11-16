import random
from hangman_words import word_list       #alternative: only "import word_list", but use from in case in hangman_words have multiple lists/variables/functions
from the_hangman_art import stages, logo 

print(logo)

#Create a variable called `lives` to keep track of the number of lives left. start with 6 lives
lives = 6

# Select a random word from the list
chosen_word = random.choice (word_list)    
print(chosen_word)  # For testing purposes





# - Create an empty String called `placeholder`.For each letter in the chosen_word, add a `_` to `placeholder`. So if the `chosen_word` was "apple", `placeholder` should be `_ _ _ _ _` with 5 `"_"` representing each letter to guess.
# - Print out `hint`.
placeholder = ""
word_length = len(chosen_word)
for letter in range(word_length):
    placeholder += " _"
print(placeholder)




game_over = False                 #boolean to control the while loop
correct_letters = []            #list to store correct guessed letters. list accumulates while the loop runs

#Get the user guess again as long as the guess is not correct, till we get the end of the script
while not game_over:
  guess = input("Guess a letter: ").lower()        #ask user to guess letters



  #Correct guess: display is the string that shows the current state of the guessed word with correct letters and blanks
  display = ""        

  for letter in chosen_word:
    if letter == guess:
      print("Good guess!")
      display += letter
      correct_letters.append(letter)                    #add correct guessed letter to the list
    elif letter in correct_letters:                        #if the letter is already guessed correctly in previous while loop before, de lan doan tiep theo blank dan dan dc fill
      display += letter
    
    else:
      display += "_"
     
  print(display)



  #repeated guess: check if the letter has been guessed before
  if guess in correct_letters:            
    print(f"You've already guessed {guess}. Try again.")
    continue


  #Wrong guess: If `guess` is not a letter in the `chosen_word`, Then reduce `lives` by `1`. If `lives` goes down to `0` then the game should end, and it should print "You lose."This step could be in else statement of for loop above, but seperate for easier debugging
  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. {lives} LIVES LEFT!!!")
    if lives == 0:
      game_over = True
      print("You lose. The correct word is:", chosen_word)
      break

  #Win condition: check if there is no more blanks in display, all letters are guessed
  if "_" not in display:                      
    print("You win!")

  #print the ASCII art from the list `stages` that corresponds to the current number of `lives` the user has remaining.
  print(stages[lives])                                          
  




