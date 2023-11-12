'''
Day 007 100
Hangman
'''
import random
from words import word_list
from art import logo
from art import stages

print(logo)
lives = len(stages)-1

word = random.choice(word_list)
print(word)
blank = []
for letter in word:
    blank.append("_")
    
letters_used = []


print(stages[lives])
print(" ".join(blank))

while lives > 0 and "".join(blank) != word:
    letter = input("Guess a letter: ")[0].lower()
    
    if letter in letters_used:
        lives -= 1
    elif letter in word:
        letters_used.append(letter)
        for i in range(len(word)):
            if letter == word[i]:
                blank[i] = letter
    else:
        letters_used.append(letter)
        lives -= 1
    
    print(stages[lives])
    print(" ".join(blank))
        
    
if "".join(blank) == word:
    print("Good job! You found the word!")
else:
    print("GAME OVER!")
    
            