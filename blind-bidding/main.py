# It's a blind bidding. No one know what others has bid. Just say highest you can pay.
# Then pass the laptop to the next bidder.
# The highest bidder wins, obviously.

import os
from art import logo

print(logo)

auction_dict = {}

def find_highest(bid_dict):
    max_bid = 0
    winner = ""
    for key in bid_dict:
        curr_bid = bid_dict[key]
        if curr_bid > max_bid:
            max_bid = curr_bid
            winner = key
    print(f"The winner is {winner} who bidded {max_bid}")


bidding_finished = False
while not bidding_finished:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  auction_dict[name] = bid
  new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if new_bidder == 'no':
    bidding_finished = True
    find_highest(auction_dict)
  elif new_bidder == "yes":  
    os.system('cls')