alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(plain_text, shift_amount, option):
  chipher_text = ""
  if option == "decode":
      shift_amount *= -1
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position +shift_amount
    chipher_text += alphabet[new_position]
  
  print(f"The {option}d text is {chipher_text}")  

caesar(text,shift,direction)