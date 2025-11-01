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
#Determine computer choice
game_image = [rock, paper, scissors]

#Map user choices names to their corresponding variables
choices_map = {"rock": rock, "paper": paper, "scissors": scissors}   #map user & computer choices to corresponding variables, match input in string to defined variables


#Determine computer choice
computer_choice = random.choice(list(choices_map.keys()))
print(computer_choice)
print(f"Computer chooses {computer_choices}")

#Determine user choice

user_choice = input("What is your choice? Type rock, paper or scissors.\n").lower()
if user_choice in map:
    print(f"You chose: {game_image [user_choice]}")
    print(f"Computer chose:\n{computer_choice}")
else: 
    print("Invalid choice. Please choose rock, paper, or scissors.")

score = 0  #both start with 0 score

#Determine winners

if user_choice == rock and computer_choices == scissors:
    print("You win!")
    score +=1

elif user_choice == rock and computer_choices == paper:
    print("You lose!")

elif user_choice == paper  and computer_choices == rock:
    print("You win!")
    score +=1

elif user_choice == paper and computer_choices == scissors:
    print("You lose!")

elif user_choice == scissors and computer_choices == paper:
    print("You win!")
    score +=1

elif user_choice == scissors and computer_choices == rock:
    print("You lose!")

elif user_choice == computer_choices:
    print("It's a draw!")
    score +=0

print(f"Your total score is: {score}")
