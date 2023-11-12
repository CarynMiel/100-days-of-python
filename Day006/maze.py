import random
options = [True, False]

def turn_left():
    print("Bot has turned left")
    
def wall_on_right():
    return options[random.choice(options)]
    
def front_is_clear():
    return options[random.choice(options)]

def move():
    print("Bot has moved forward")
    
def at_goal():
    return options[random.choice(options)]

def turn_right():
    for i in range(3):
        turn_left()
def main():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

while not at_goal():
    main()