#Coding Challenge
#Task Auction Program
#Input: CHeck bidder and put bid
#Output: Win or loss

import pyfiglet
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def findMax(record):
    max_bid = 0
    winner = ""
    for bidder, bid_amount in record.items():
        bid_amt_int = int(bid_amount)
        if bid_amt_int > max_bid:
            max_bid = bid_amt_int
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")

hammer = '''
                   ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
        '''
print(hammer)
print(pyfiglet.figlet_format("Welcome to Auction Program"))

dictBid = {
    'A': '100',
    'B': '101',
    'C': '110',
    'D': '104',
}
max_bid = 0
print('Bidding price started from $100')
biddingFin = False

while not biddingFin:
    name = input("What is your name? ")
    bidPrice = int(input('What is your bid?: $'))
    dictBid[name] = str(bidPrice)
    decision = input("Are there any other bidders? yes or no\n")
    if decision.lower() == 'no':
        biddingFin = True
        findMax(dictBid)
    elif decision.lower() == 'yes':
        clear()
