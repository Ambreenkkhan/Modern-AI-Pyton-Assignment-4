import random

# User guesses the computer's number
def guess(x):
    # Generate random number between 1 and x
    random_number = random.randint(1, x)
    guess = 0  # Initialize guess variable
    
    # Loop until user guesses correctly
    while guess != random_number:
        # Get user's guess
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        # Provide feedback on the guess
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    
    # Congratulate when correct
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')


# Start the user-guessing game with range 1-10
guess(10)
