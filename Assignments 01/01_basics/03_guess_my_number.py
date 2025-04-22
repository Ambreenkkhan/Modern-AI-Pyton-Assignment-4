import random  # Importing random module to generate a random number

def main():
    # Generate a random number between 0 and 99 (inclusive)
    secret_number = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    # Ask the user for their first guess
    guess = int(input("Enter a guess: "))

    # Keep looping until the user guesses correctly
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")

        # Ask for another guess
        guess = int(input("Enter a new number: "))

    # When the loop ends, the correct number was guessed
    print(f"Congrats! The number was: {secret_number}")

# Run the main function
if __name__ == "__main__":
    main()
