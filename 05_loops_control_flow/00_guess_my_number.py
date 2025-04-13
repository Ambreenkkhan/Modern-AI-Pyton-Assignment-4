import random

def main():
    # Randomly generate a secret number between 1 and 50
    secret_number = random.randint(1, 50)

    print("I am thinking of a number between 1 and 50...")

    # Ask the user for their first guess
    guess = int(input("Enter a guess: "))

    # Keep asking until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        print()  # Add a blank line for better readability
        guess = int(input("Enter a new guess: "))

    # User guessed correctly
    print(f"Congrats! The number was: {secret_number}")

if __name__ == '__main__':
    main()
