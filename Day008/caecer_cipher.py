'''
Day 008/100
Caecer Cipher
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")[0].lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "e":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
            
def code(shift):
    encode = []
    for i in range(len(alphabet)-shift):
        if i + shift< len(alphabet):
            encode.append(alphabet[i + shift])
    for i in range(shift):
        encode.append(alphabet[i])
    return encode

def encrypt(text, shift):
    encode = code(shift)
    word = []
    for letter in text:
        index = alphabet.index(letter)
        word.append(encode[index])
    word = "".join(word)
    print(f"Here is the encoded message: {word}")
        
def decrypt(text, shift):
    decode = code(shift)
    
    word = []
    for letter in text:
        index = decode.index(letter)
        word.append(alphabet[index])
    word = "".join(word)
    print(f"Here is the decoded message: {word}")
    
while True:
    main()
    
    again = input("Do you want to go again?: ")[0].lower()
    while again != "y" and again != "n":
        again = input("That is not an option. (yes or no): ")[0].lower()
    
    if again == "y":
        continue
    else:
        break

print("Have a good day!")

