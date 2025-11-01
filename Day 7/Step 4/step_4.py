stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


import random

#Create a variable called `lives` to keep track of the number of lives left. start with 6 lives
lives = 6

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


game_over = False                 #boolean to control the while loop
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



  ### TODO-2: 
  # - If `guess` is not a letter in the `chosen_word`, Then reduce `lives` by `1`. 
  # - If `lives` goes down to `0` then the game should end, and it should print "You lose."This step could be in else statement of for loop above, but seperate for easier debugging
  if guess not in chosen_word:
      lives -= 1
      game_over = True
      print("You lose")
      break


  if "_" not in display:                      #there is no more blanks, all letters are guessed
    game_over = True
    print("You win")

  print(stages[lives])                                          #print the ASCII art from the list `stages` that corresponds to the current number of `lives` the user has remaining.
  

### TODO-1: 
# - Create a variable called `lives` to keep track of the number of lives left.
# - Set `lives` to equal `6`.


### TODO-2: 
# - If `guess` is not a letter in the `chosen_word`, Then reduce `lives` by `1`. 
# - If `lives` goes down to `0` then the game should end, and it should print "You lose."

# <div class="hint">
#   The not in keywords will be your friend in this todo. You can check if something exists in the chosen_word completely separately from the rest of the code.
# </div>


### TODO-3: 
# - print the ASCII art from the list `stages` that corresponds to the current number of `lives` the user has remaining.