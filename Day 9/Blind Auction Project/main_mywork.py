from art import logo
print (logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


auction = {}  #create dictionary       auction = {"name": bid}, "name" is key, bid is value


#Define function:   
def define_winning_bidder():
    highest_bid = 0        #start from 0
    winner = ""      #list of winners in case there more than one highest bids, or winners = []??

    for name, bid in auction.items():      #items() return key-value pairs from dictionary
        if bid > highest_bid:
            highest_bid = bid
            winner = name      #use the name, if auction [name], is value, if there are two highest bids, create a list
        elif bid == highest_bid:
            winner.append(name)

#Printing final result: 
    print(f"The winner is {winner} with a bid of ${highest_bid}")


#start here
# should_continue= input("Are there any other bidders Type 'yes' or 'no' \n")

continue_auction = True
while continue_auction:
    name = input("What is your name? \n ")
    bid = int(input("What is your bid?\n"))
    auction[name] = bid      ##target dict: {"Alice": 100, "Bob": 250}, summarized from: price = int(input("What is your bid?\n")) , auction [name ]= price
    should_continue = input("Are there any other bidders Type 'yes' or 'no' \n").lower()
    print("\n"*100)                  #keep each bidder secret
    
    if should_continue == "no":
        define_winning_bidder()
        break
        #print ("All bids: ", auction)      #for testing purposes
    
    



#Printing auction result:
# if len(winners) ==1:
#     print(f"The winner is {winners[0]} with a bid of €{highest_bid}.")
# else:
#     print (f"Its a tie! Winners: {', '.join(winners) } with a bid of €{highest_bid}")



#problem 1: delete asking first

