alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))





# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    cipher_text = ""

    #shift each letter of the original_text forwards in the alphabet by the shift amount
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position >= len(alphabet):    #Fix for shifting beyond 'z'
                new_position = new_position - len(alphabet)   #Wrap around the alphabet. 
                #new_position = new_position - len(alphabet) subtracts 26 once to "wrap" past 'z'. That works for small shifts (e.g. 'z' + 9 → 25+9=34 → 34-26=8 → 'i').
            
            # alternative: new_position = new_position % len(alphabet)   #Modulo operator to wrap around the alphabet for any shift size.



            cipher_text += alphabet[new_position]         #add the new shifted character to encrypted_text
        
        else:
            cipher_text += char      #if character is not in alphabet (like space, punctuation_dau cau), just add it as it is.
    
    print(f"The encoded text is {cipher_text}")
    

encrypt(original_text = text, shift_amount = shift)      #keyword arguments
#or encrypt (text, shift)    #positional arguments
   
   
   
   

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

