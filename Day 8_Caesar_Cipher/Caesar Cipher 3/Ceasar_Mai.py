#This is my version, try coding Cesar from scratch again
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#def ceasar (original_text, shift_amount, direction):

# def encode(text, shift):
#     cipher_text = ""            #van ban mat ma, alternative: output_text
#     for char in alphabet:
#         position = alphabet.index(char)
#         new_position = str((position + shift)% len(alphabet))
#         print (f"Your encoded result is {cipher_text}.")

#Restart the ceasar:
should_continue = True
while True:
    ask = input ("Do you want to restart. Type 'yes' to continue and 'no' to exit: ").lower()
    if ask == "yes":
        #Ask for user input to set up cipher
        text = input ("What is you message? \n"). lower()
        shift = int(input("Type the shift number: \n"))
        direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"). lower()
    
    else:
        should_continue= False 
        print ("Goodbye!")



def ceasar (original_text = text, shift_amount = shift, encode_or_decode = direction):
    output_text = ""                #create a string to store output text for each char to be released 


    if direction == "decode":
        shift *= -1        #shift_amount  reversed 
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)      #index () to retrieve the position of a char in a [alphabet ] list
            new_position = (position + shift) % len(alphabet)       #wrap up if char lies in z
            output_text += alphabet[new_position]

        else: 
            output_text += char                 #just pass through if char is space/ punctuation . ,
    print (f"Your {encode_or_decode}d result is: {output_text}")

ceasar (original_text = text, shift_amount = shift, encode_or_decode = direction)

# def encrypt(original_text = text , shift_amount = shift):                   #keyword arguments
#     cipher_text = "" 

#     for char in text:   # iterate the user input, loop through the text that user types (not the alphabet list!)
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = (position + shift)
#             cipher_text += alphabet[new_position]                     #indexing from alphabet list

#         else: 
#             cipher_text += char            #just add space/ punctuation as it is

#     print (f"Your encoded result is: {cipher_text}")


# encrypt(original_text = text, shift_amount = shift)    



# def decrypt(original_text = text, shift_amount = shift):
#     decipher_text = "" 

#     for char in text:   # iterate the user input, loop through the text that user types (not the alphabet list!)
#         if char in alphabet:
#             position = alphabet.index(char)     
#             new_position = (position - shift)
#             decipher_text += alphabet[new_position]                     #indexing from alphabet list

#         else: 
#             decipher_text += char            #just add space/ punctuation as it is

#     print (f"Your decoded result is: {decipher_text}")

# decrypt(original_text = text, shift_amount = shift) 



