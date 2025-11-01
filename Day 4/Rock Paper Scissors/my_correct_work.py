import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



#Map user choices names to their corresponding variables
#Vi ko chon cach use integer (0,1,2) to distinguish r,p,s so I map string inputs to corresponding variables
choices_map = {"rock": rock, "paper": paper, "scissors": scissors}   #map user & computer choices to corresponding variables, match input in string to defined variables


#Determine computer choice
computer_choice = random.choice(list(choices_map.keys()))    #keys() returns a view object that displays a list of all the keys in the dictionary. By converting it to a list, we can use random.choice() to select one of the keys randomly. This output is in string format.
#print(f"Computer chooses: \n{choices_map[computer_choice]}.")  - this will print the ASCII art corresponding to the computer's choice.

#Determine user choice
user_choice = input("What is your choice? Type rock, paper or scissors.\n").lower()
if user_choice in choices_map:
    print(f"You chose: {choices_map [user_choice]}")

else: 
    print("Invalid choice. Please choose rock, paper, or scissors.")

score = 0  #both start with 0 score

#Determine winners
# rules: rock beats scissors, scissors beats paper, paper beats rock
wins_against = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

if user_choice == computer_choice:
    print("It's a draw!")
elif wins_against[user_choice] == computer_choice:
    print("You win!")
    score +=1   
else:
    print("You lose!")

print(f"Computer choose {choices_map[computer_choice]}.")  # correct: call print with parentheses
print(f"Your total score is: {score}")
