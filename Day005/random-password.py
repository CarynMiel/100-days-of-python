# Day 005/100
# Random Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numLetters = int(input("How many letters are in your password?: "))
numNumbers = int(input("How many numbers are in your password?: "))
numSymbols = int(input("How many symbols are in your password?: "))

# Easy - Random characters
easy = []
for letter in range(numLetters):
    
    easy.append(letters[random.randrange(0,len(letters))])
for number in range(numNumbers):
    easy.append(numbers[random.randrange(0,len(numbers))])
for symbol in range(numSymbols):
    easy.append(symbols[random.randrange(0,len(symbols))])
epass = "".join(easy)
print(f"Your easy password is :\"{epass}\"")

# Hard - Random order
hard = []
for item in range(len(easy)):
    index = random.randrange(0,len(easy))
    character = easy[index]
    easy.remove(easy[index])
    hard.append(character)
hpass = "".join(hard)
print(f"Your hard password is: \"{hpass}\"")
