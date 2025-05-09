import random

# Computer guesses the user's number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # only one possible number left
        
        # User gives feedback: 'h' if too high, 'l' if too low, 'c' if correct
        feedback = input(f'Is {guess} too high (h), too low (l), or correct (c)? ').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'waoo! The computer guessed your number {guess} correctly!')

# Start the computer-guessing game with range 1-10
computer_guess(10)
