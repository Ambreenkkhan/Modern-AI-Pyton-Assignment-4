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

# Computer guesses user's number
def computer_guess(x):
    low = 1     # Minimum possible value
    high = x    # Maximum possible value
    feedback = ''  # User feedback (H/L/C)
    
    # Continue until computer guesses correctly
    while feedback != 'c':
        # Generate guess within current possible range
        if low != high:
            guess = random.randint(low, high)
        else:
            # When range narrows to single number
            guess = low  # could also be high b/c low = high
        
        # Get user feedback
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        
        # Adjust search range based on feedback
        if feedback == 'h':
            high = guess - 1  # Set new upper bound
        elif feedback == 'l':
            low = guess + 1   # Set new lower bound

    # Final success message
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

# Start the user-guessing game with range 1-10
guess(10)
