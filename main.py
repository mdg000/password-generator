# 100 Days of Code Practice Project
# Password Generator 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# User defines the size and composition of password
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# grab random characters from each list, creating a single string password
rnd_letters = ""
for letter in range(nr_letters):
  rnd_letters += random.choice(letters)
rnd_symbols = ""
for letter in range(nr_symbols):
  rnd_symbols += random.choice(symbols)
rnd_numbers = ""
for letter in range(nr_numbers):
  rnd_numbers += random.choice(numbers)
password = rnd_letters + rnd_symbols + rnd_numbers

# scrambles the final password
scramble = ""
for i in password:
  scramble += random.choice(password)
print(scramble)
