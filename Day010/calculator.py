from art import logo
print(logo)

def main():
    option = "y"
    
    while option != "e":
        x = float(input("What's the first number?: "))
        operation = input("[+], [-], [*], [/]\nPick an operation: ")
        y = float(input("What's the second number?: "))
        
        ans = calc(x, operation, y)
        
        print(f"{x} {operation} {y} = {ans}")
        
        option = input(f"[yes]  to continue with {ans}\n[no]   to start a new operation\n[exit] to exit the program\nWhat do you want to do?: ")[0].lower()

        if option == "n":
            continue
        elif option == "y":
            x = ans
            operation = input("[+], [-], [*], [/]\nPick an operation: ")
            y = float(input("What's the second number?: "))
            
            ans = calc(x, operation, y)
        
            print(f"{x} {operation} {y} = {ans}")
            
            

def calc(x, operation, y):
    return float(eval("{} {} {}".format(x, operation, y)))


main()