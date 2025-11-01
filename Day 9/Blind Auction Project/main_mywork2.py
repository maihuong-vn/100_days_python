import art
print(art.logo)

bids = {}      #create dictionary

def find_highest_bidder(bids):
    winner = ""
    highest_bid = 0

    #ALERNATIVE
    # for bidder in bids:
    #     bid_amount = bids[bidder]      #value = dict[key], retrieve value from key
    #     if bid_amount > highest_bid:
    #         highest_bid = bid_amount
    #         winner = bidder

    winner = max(bids, key = bids. get)
    highest_bid = bids [winner]
    
    print(f"The winner is {winner} with a bid of € {highest_bid}.")




#start here

continue_bidding = True
while continue_bidding:
    name = input("What is your name?\n")
    price = int(input("What is your bid: €"))
    bids[name] = price     #dict[key]= value
    should_continue = input("Are there any other bidders Type 'yes' or 'no'. \n ")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder (bids)
    elif should_continue == "yes":
        print("\n" *50)                    #enter a lot to hide info
max (bids, key= bids.get)

