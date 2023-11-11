'''
Day 002/100 
Tip Calculator
'''

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: $"))
tip = int(input("How much tip would you like to give?: ")) / 100
people = int(input("How many people to split the bill?: "))
pay = (bill * (1+tip)) / people
pay = "{:.2f}".format(pay)
print(f"Each person should pay: ${pay}")
