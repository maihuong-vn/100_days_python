import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# passwords = ""         #create an empty string to add characters to it
# for char in range (1, nr_letters + 1):
#     passwords +=random.choice(letters)    #choose random letter from letters list and add it to passwords string     
#     print(passwords)

# for char in range (1, nr_symbols + 1):
#     passwords +=random.choice(symbols)
#     print(passwords)

# for char in range (1, nr_numbers +1):
#     passwords +=random.choice(numbers)      
#     print(passwords)


# print("Your password is: " + passwords)
#we want outout in complete random order not in the order of letters, symbols and numbers

password_list = []
for char in range (0, nr_letters):
    password_list.append(random.choice(letters))    #choose random letter from letters list and add it to passwords string

for char in range (0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range (0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)   #to shuffle the list containing letters, numbers, symbols so that the order of characters is random

password = ""   #change into string
for char in password_list:
    password += char    

print("Your password is: " + password)
                         
