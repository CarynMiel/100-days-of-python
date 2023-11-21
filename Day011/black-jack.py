# Day 011/100
# Project: Black Jack
import random

import os
clear = lambda: os.system('clear')
clear()

def main():
    play = input("Do you want to play Black Jack?: ")[0].lower()

    while play != "n" and play != "y":
        play = input("That is not an option. YES or NO?: ")

    if play == "n":
        print("Ok bye!")
        quit()
    else:
        game()

def game():
    clear()
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]
    pscore = player[0] + player[1]
    
    computer = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]
    cscore = computer[0] + computer[1]
    while cscore < 11:
        computer.append(cards[random.randrange(0, len(cards))])
        cscore += computer[len(computer)-1]
    
    print(f"Your cards are: {player}\nYour score is: {pscore}")
    print(f"The computer's first card was: {computer[0]}\n")
    play = "h"
    
    while play != "s":
        play = input("Hit (get another card) or stand (keep current cards)?: ")[0].lower()
        
        while play != "h" and play != "s":
            play = input("That is not an option. HIT or STAND")
            
        if play == "s":
            print(f"Your final score was: {pscore}")
            print(f"Computer's score was: {cscore}")
            checker(pscore, cscore)
            
        else:
            player.append(cards[random.randrange(0, len(cards))])
            pscore += player[len(player)-1]
            if pscore > 21:
                checker(pscore, cscore)
            print(f"Your cards are: {player}\nYour score is: {pscore}")
            print(f"The computer's first card is: {computer[0]}")
            continue

def checker(player, computer):
    if player > 21:
        print("You lose! It was a bust")
    elif computer > 21:
        print("You Win! The computer get a bust")
    elif player > computer:
        print("You Win! You got a closer score to 21")
    else:
        print("You Lose! The computer got a closer score to 21")
    quit()
        
main()