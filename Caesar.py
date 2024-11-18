alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
# def decrypt(original_text,shift_amount):
#     cipher_text =""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {cipher_text}")


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if encode_or_decode == "decode":
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        elif encode_or_decode == "encode":
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            print("Invalid direction. Please type 'encode' or 'decode'.")

    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue =True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart=input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == 'no':
        should_continue = False
        print('Goodbye.')




