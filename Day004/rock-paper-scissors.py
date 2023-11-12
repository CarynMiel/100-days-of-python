'''
Day 004/100
Rock Paper Scissors
'''

print(''' What do you choose?
0 Rock
1 Paper
2 Scissors
      ''')
import random

choices = [
'''Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]
player = int(input())
computer = random.randrange(0,3)
print(f"Your choise: {choices[player]}")
print(f"Computer's choice: {choices[computer]}")

if player == 0 and computer == 2 or player == 1 and computer == 0 or player == 2 and computer == 1:
    print("You win")
elif player == 2 and computer == 0 or player == 0 and computer == 1 or player == 1 and computer == 2:
    print("You lose")
else:
    print("It's a draw")