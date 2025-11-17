#this code is not AI generated, 100% written by human, I only asked ChatGPT how to do things generally, I designed architecture and know what to do    
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]      #this is a list

'''Step 1: Deal both user and computer a starting hand of 2 random card values'''

#Define function hit (draw another card)
def hit(player_cards):     #add a new random card to player and print updated score
    picked_number = random.choice(cards)
    player_cards.append(picked_number)
    player_score = sum(player_cards)
    print (f"Your cards: {player_cards}, current score: {player_score}")
    return player_score                         #have to return, or else value not stored in next function!

#Check bust
def check_bust(player_score):
    if player_score > 21:
        print (f"Your final hand: {player_cards}, final score: {player_score} \n Computers final hand: {computer_cards}, final score: {computer_score}")
        print ("You went over. You lose 😭")
    elif player_score == 21:
        print ("You get Blackjack!")
    elif player_score and computer_score <= 21 and computer_score > player_score:
        print ("You lose 😤")
    elif player_score and computer_score <= 21 and player_score > computer_score:
        print ("You win!")



should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if should_continue == "y":
    player_cards = []

    #Draw on 2 cards to player
    player_cards.extend(random.choices(cards, k=2))      #add picked number into play_card list, not use append to avoid double [[]], extend add elements individually
    player_score = sum (player_cards)
    print (f"Your cards: {player_cards}, current score: {player_score}")

    
    #Computer gets a hand, we only show its first card initially
    computer_cards = []
    computer_cards.extend(random.choices(cards, k= 2))              #Initially both player & computer get 2 cards from the dealer!
    computer_score = sum (computer_cards)
    print(f"Computer's first card: {computer_cards[0]} ")          #create a list for computer cards, but show only one card, use index [0]
    #add else statement to stop if "n"??



    #Ask player to hit (draw another card) or stand (not drawing and let computer fold)
    should_hit = input("Type 'y' to get another , type 'n' to pass: ")
    if should_hit == "y":
        player_score = hit(player_cards)       #captured return score.This way, stored value in previous function will be accumulated
    print(f"Computer's first card: {computer_cards[0]} ")        #Should I show 1 or both cards computer have, should comp draw also along with player??
    #add else statement to stop if "n"



check_bust (player_score)
'''Step 2: Check bust??'''


'''Next to-do: order check_bust function where? from the starts?
print(f"Computer's first card: {computer_cards[0]} ")        #Should I show 1 or both cards computer have, should comp draw also along with player??
    #the amount of cards in players hand depends on player decision to draw another card or lat bai, create a while loop to ask player?'''

