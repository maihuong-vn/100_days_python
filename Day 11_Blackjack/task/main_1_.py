#this code is not AI generated, 100% written by human, I only asked ChatGPT how to do things generally, I designed architecture and know what to do    
#this version includes code block that have mistakes in #
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]      #this is a list

# I. Deal both user and computer a starting hand of 2 random card values
#Define function hit (draw another card)
def hit(player_cards):     #add a new random card to player and print updated score
    picked_number = random.choice(cards)
    player_cards.append(picked_number)
    player_score = sum(player_cards)
    print (f"Your cards: {player_cards}, current score: {player_score}")
    return player_score                         #have to return, or else value not stored in next function!


def calculate_score (cards):
    score = sum (cards)

    ## Wenn ein Ass (11) drin ist und Score > 21 → Ace wird zu 1
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1         #Finde die erste Karte in der Liste, die den Wert 11 hat (aka ein Ass) und ersetze sie durch 1
        score = sum (cards)  #recalculate the sum with Ass changed = 1
    
    return score



should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if should_continue == "y":
    player_cards = []

    #Draw on 2 cards to player
    player_cards.extend(random.choices(cards, k=2))      #add picked number into play_card list, not use append to avoid double [[]], extend add elements individually
    #player_score = sum (player_cards)
    #print (f"Your cards: {player_cards}, current score: {player_score}")

    
    #Computer gets a hand, we only show its first card initially
    computer_cards = []
    computer_cards.extend(random.choices(cards, k= 2))              #Initially both player & computer get 2 cards from the dealer!
    #computer_score = sum (computer_cards)
    print(f"Computer's first card: {computer_cards[0]} ")          #create a list for computer cards, but show only one card, use index [0]
    #add else statement to stop if "n"??



    #Ask player to hit (draw another card) or stand (not drawing and let computer fold)
    should_hit = input("Type 'y' to get another , type 'n' to pass: ")
    if should_hit == "y":
        player_score = hit (player_cards)       #use hit() which appends and returns new score
        print(f"Computer's first card: {computer_cards[0]} ")        #Should I show 1 or both cards computer have, should comp draw also along with player??
    else:
    # ensure we still have up-to-date score if player stands
        player_score = calculate_score(player_cards)

    if player_score > 21:
        print("Bust! You lose 😭")
        quit()


def is_blackjack(cards):
    return len(cards) == 2 and calculate_score (cards) ==21  #prüft ob es genau zwei Karten gibt UND die beiden Karten Summe ==21 , also check ein Blackjack


def determine_winner (player_cards, computer_cards):
    player_score = calculate_score(player_cards) #anstatt sum(player_score), wegen kompliziertes Ass Regel, ab 2.mal Ass = 1 & Wenn SUmme über 21, Ass = 1
    computer_score = calculate_score(computer_cards)
    player_blackjack = is_blackjack(player_cards)
    computer_blackjack = is_blackjack(computer_cards)

    if player_blackjack or computer_blackjack:
        print (determine_winner(player_cards, computer_cards))
        quit()

# II. Determine winner: There are 3 cases_blackjack case (one of us hit BJ), bust case, normal comparison
#1. Blackjack case:

    if computer_blackjack and player_blackjack:
        return "You lose 😤 Dealer wins tie with Blackjack"
    if computer_blackjack:
        return "You lose 😤, Dealer has Blackjack"
    if player_blackjack:
        return "You win! 😁, YOU have Blackjack"

#2. Bust case: cards value larger than 21, then lose
    if player_score > 21:
        return "Bust! You lose 😭"
    if computer_score > 21:
        return "Dealer busts. You win! 😁"


#3. Normal comparison:
    if player_score > computer_score:
        return "You win!"
    elif player_score < computer_score:
        return "You lose 😤"
    else: 
        return "Draw."

#To-DO: 
#  - If type 'n', reveal all card of player & computer: "Your final hand, final score. Computers final hand, final score"
#  -Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.
#  - Print out the player's and computer's final hand and their scores at the end of the game.
#  - After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.


'''check_bust (player_score)
#Check bust
def check_bust(player_score): this is operational, I cant write 10+ blocks of elif # this does not cover ALL cases yet!
    if player_score > 21:
        print (f"Your final hand: {player_cards}, final score: {player_score} \n Computers final hand: {computer_cards}, final score: {computer_score}")
        print ("You went over. You lose 😭")
    elif player_score == 21:
        print ("You get Blackjack!")
    elif player_score and computer_score <= 21 and computer_score > player_score:
        print ("You lose 😤")
    elif player_score and computer_score <= 21 and player_score > computer_score:
        print ("You win! 😁")'''
