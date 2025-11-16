#this code is not AI generated, 100% written by human, I only asked ChatGPT how to do things generally, I designed architecture and know what to do    
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]      #this is a list


should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if should_continue == "y":
    player_cards = []
    #how to draw on 2 cards initially???
    picked_numbers = random.choices(cards, k=2)    #this is already a list, so it is in form: [abc]
    player_cards.extend(picked_numbers)      #add picked number into play_card list, not use append to avoid double [[]], extend add elements individually
    #print(player_cards)                             #testing the list
    player_score = sum (player_cards)
    print (f"Your cards: {player_cards}, current score: {player_score}")

    #do the same for computer first draw
    #add else statement to stop if "n"

    #the amount of cards in players hand depends on player decision to draw another card or lat bai, create a while loop to ask plyer?