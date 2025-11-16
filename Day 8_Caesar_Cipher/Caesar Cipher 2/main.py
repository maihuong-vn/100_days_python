alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# #Encode function
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")


# #encrypt(original_text=text, shift_amount=shift)



# # TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
# #  by the shift amount and print the decrypted text.
# # TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
# #  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def decrypt(original_text, shift_amount):

#     decipher_text = ""

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount  #turn backwards by subtracting shift_amount
#         shifted_position %= len(alphabet)
#         decipher_text += alphabet[shifted_position]     #add the new shifted character to decrypted_text
#     print(f"The decoded text is {decipher_text}")


# decrypt(original_text=text, shift_amount=shift)



#ceasar function combining both encrypt and decrypt above
def ceasar(original_text, shift_amount, encode_or_decode):      #new direction parameter
    output_text= ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1      #turn backwards by multiplying shift_amount by -1, changeing its value in opposite direction

        shifted_position = alphabet.index(letter) + shift_amount #+ shift_amount bc if decode, shift_amount is negative *= -1 above!
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")



ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)
#alternative call: ceasar(text, shift, direction)   #positional arguments
