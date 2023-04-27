alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amt, dir):
    text = ""
    if dir == "decode":
        shift_amt *= -1
    for char in start_text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos + shift_amt
            text += alphabet[new_pos]
        else:
            text += char
    print(f"The {dir}d text is {text}")


play_again = True

while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amt=shift, dir=direction)
    print("Play again?")
    replay = input("(y) to play again. (n) to quit.\n")
    if replay == 'n' or replay == "N":
        print("Goodbye")
        play_again = False


# OR


# def encode(plain_text, shift_amt):
#     cypher = ""
#     for letter in plain_text:
#         pos = alphabet.index(letter)
#         new_pos = pos + shift_amt
#         new_letter = alphabet[new_pos]
#         cypher += new_letter
#     print(f"The encoded text is {cypher}")

# def decode(cypher, shift_amt):
#     plain_text = ""
#     for letter in cypher:
#         pos = alphabet.index(letter)
#         new_pos = pos - shift_amt
#         plain_text += alphabet[new_pos]
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encode(plain_text=text, shift_amt=shift)
# elif direction == "decode":
#     decode(cypher=text, shift_amt=shift)
