# Day 011/100
# Project: Black Jack
import random

def main():
    play = input("Do you want to play Black Jack?: ")[0].lower()

    while play != "n" and play != "y":
        play = input("That is not an option. YES or NO?: ")

    if play == "n":
        print("Ok bye!")
        quit()
    else:
        play()

def play():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]
    pscore = player[0] + player[1]
    
    computer = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]
    cscore = computer[0] + computer[1]
    
    print(f"Your cards are: [{player[0]}, {player[1]}]\nYour score is: {pscore}")
    print(f"The computer's first card was: {computer[0]}\n")
    
    play = input("Hit (get another card) or stand (keep current cards)?: ")[0].lower()
    
    while play != "h" and play != "s":
        play = input("That is not an option. HIT or STAND")
        
    if play == "s":
        print(f"Your final score was: {pscore}")
        print(f"Computer's score was: {cscore}")
        
    else:
        player.append(cards[random.randrange(0, len(cards))])
        
main()