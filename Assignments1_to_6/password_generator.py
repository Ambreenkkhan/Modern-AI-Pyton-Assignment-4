print('\n"Password_Generator"\n')

# Import the random module to randomly select characters
import random

# Define the set of characters allowed in the password
chars_options = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'

# Ask the user how many passwords they want to generate
num = int(input('How many passwords would you like to generate? ')) 

# Ask the user how long each password should be
length = int(input('\nEnter your password length: '))

# Print a message to indicate the generated passwords are coming next
print('\nYour passwords are:')

# Outer loop runs 'num' times to generate the required number of passwords
for i in range(num):
  passwords = ''  # Initialize an empty string to store the password
  # Inner loop runs 'length' times to build a password of desired length
  for j in range(length):
    passwords += random.choice(chars_options)  # Add a random character to the password
  print(passwords)  # Print the generated password
