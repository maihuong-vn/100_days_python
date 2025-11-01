#This is my version, try coding Cesar from scratch again
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Ask for user input to set up cipher
# text = input ("What is you message? \n"). lower()
# shift = int(input("Type the shift number: \n"))
# direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"). lower()




#Lesson: define input in function, use the EXACT INPUT inside that function

def ceasar (original_text, shift_amount, encode_or_decode):          #input I call it myself. Outside when call ceasar (), have to use keyword_arguments to match shift = shift_amount, etc. 
    output_text = ""                #create a string to store output text for each char to be released 


    if encode_or_decode == "decode":
        shift_amount *= -1        #shift_amount  reversed, not use shift, bc ceasar () function define shift_amount = shift variable outside, so inside ceasar() I should use shift_amount instead. If I wanna use shift inside ceasar(), I should define ceasar (text, shift, direction)
    
    for char in original_text:       #for char in original
        if char in alphabet:
            position = alphabet.index(char)      #index () to retrieve the position of a char in a [alphabet ] list
            new_position = (position + shift_amount) % len(alphabet)       #wrap up if char lies in z
            output_text += alphabet[new_position]

        else: 
            output_text += char                 #just pass through if char is space/ punctuation . ,
    print (f"Your {encode_or_decode}d result is: {output_text}")





#(Re)start the ceasar:
should_continue = True
while True:
    
    #While true, keep asking for user input to set up cipher
    text = input ("What is you message? \n"). lower()
    shift = int(input("Type the shift number: \n"))
    direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"). lower()
    
    ceasar (original_text = text, shift_amount = shift, encode_or_decode = direction)     #keyword_arguments, match variable with input side def ceasar ()

    restart = input ("Do you want to restart. Type 'yes' to continue and 'no' to exit: ").lower()
    if restart != "yes":
        should_continue= False 
        print ("Goodbye!")