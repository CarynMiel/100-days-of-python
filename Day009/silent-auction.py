import os
clear = lambda: os.system('clear')

from art import logo
print(str(logo))

print("Welcome to the secret auction program.")
auction = {}
another = "y"

while another == "y":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    auction[name] = bid
    
    another = input("Is there another bider? (yes or no): ")[0].lower()
    if another == "y":
        clear()
        
max_bid = 0
max_bidder = ""
for key in auction:
    if auction[key] > max_bid:
        max_bidder = key
        max_bid = auction[key]

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")