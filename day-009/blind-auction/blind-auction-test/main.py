# # from replit import clear
# # # HINT: You can call clear() to clear the output in the console.

# from art import logo
# print(logo)

# name = input("What is your name?: ").lower()
# bid = int(input("What is your bid price?: $"))

# user_log = []
# def auction_player(user_name, user_bid):
#     auction = {}
#     auction["name"] = user_name,
#     auction["bid"] = user_bid,
#     user_log.append(auction)

# add_user = input("Is there another user who want to bid? Yes/No: ").lower()

# user_input = True
# while user_input:
#     if add_user == "No":
#         result = max(bid)
#     else:
#         user_input = False

# auction_player(user_name = name, user_bid = bid)
# print(user_log)


### SOLUTION:
# from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    continue