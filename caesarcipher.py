alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount

#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]

#     print(f"Here is the encoded result: {cipher_text}")


# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount

#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]

#     print(f"Here is the decoded result: {cipher_text}")


def ceaser(original_text, shift_amount, endode_or_decode):
    output_text = ""
    for letter in original_text:
        if endode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {endode_or_decode}d result: {output_text}")
    # if endode_or_decode == "encode":
    #     encrypt(text, shift)
    # elif direction == "decode":
    #     decrypt(text, shift)
    # else:
    #     print("Invalid direction. Please type 'encode' or 'decode'.")


ceaser(original_text=text, shift_amount=shift, endode_or_decode=direction)
