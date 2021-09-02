#HINT: You can call clear() to clear the output in the console.
from replit import clear
from art import logo

# Dictionary for the bids
bid_dict = {}

# Add entry do bid dictionary
def add_bid(name, bid):
  bid_dict[name] = bid

# Find and print the highest bid
def find_highest_bid():
  highest_bid = 0
  name_winner = ""
  for name in bid_dict:
    if bid_dict[name] > highest_bid:
      highest_bid = bid_dict[name]
      name_winner = name
  print(f"The winner is {name_winner} with a bid of ${highest_bid}.")

print(logo)
keep_bidding = True

while keep_bidding:
  user_name = input("What is your name? ")
  user_bid = int(input("What's your bid? $"))
  add_bid(name=user_name, bid=user_bid)
  other_bids = input("Are there any other bids? Type 'yes' or 'no'. ")

  if other_bids == "yes":
    keep_bidding = True    
  else:
    keep_bidding = False    
  clear()

find_highest_bid()
