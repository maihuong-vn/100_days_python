import random

# Define ASCII art
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

# Map user inputs to corresponding ASCII art
map_choices = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# List form for random computer choice
game_images = [rock, paper, scissors]
computer_choice = random.choice(list(map_choices.keys()))

score = 0

# --- User input ---
user_choice = input("What is your choice? Type rock, paper or scissors:\n").lower()

if user_choice not in map_choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    print(f"You chose:\n{map_choices[user_choice]}")
    print(f"Computer chose:\n{map_choices[computer_choice]}")

    # --- Determine winner ---
    if user_choice == computer_choice:
        print("It's a draw!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        score += 1
    else:
        print("You lose!")

    print(f"Your total score is: {score}")
