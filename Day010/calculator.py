# Day 010/100
# Basic Text Calculator

import os
clear = lambda: os.system('clear')
clear()

from art import logo

def main():
    clear()
    print(logo)
    option = "y"
    
    while option != "e":
        x = float(input("What's the first number?: "))
        operation = input("[+], [-], [*], [/]\nPick an operation: ")
        y = float(input("What's the second number?: "))
        
        ans = calc(x, operation, y)
        
        print(f"\n{x} {operation} {y} = {ans}\n")
        
        option = input(f"[yes]  to continue with {ans}\n[no]   to start a new operation\n[exit] to exit the program\nWhat do you want to do?: ")[0].lower()

        if option == "y":
            x = ans
            operation = input("[+], [-], [*], [/]\nPick an operation: ")
            y = float(input("What's the next number?: "))
            
            ans = calc(x, operation, y)
            
            print(f"\n{x} {operation} {y} = {ans}\n")
            
            option = input(f"[yes]  to continue with {ans}\n[no]   to start a new operation\n[exit] to exit the program\nWhat do you want to do?: ")[0].lower()
            
        else:
            main()
          
    print("Thanks for playing")
    exit()
            
            

def calc(x, operation, y):
    return float(eval("{} {} {}".format(x, operation, y)))


main()