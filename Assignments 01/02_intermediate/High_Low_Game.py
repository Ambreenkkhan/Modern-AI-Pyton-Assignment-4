import random  # Import the random module to generate random numbers

# Set the number of rounds to play
NUM_ROUNDS = 5

def main():
    print("Welcome to the High Low Game")
    print("*****************************")

    # Initialize your score
    your_score = 0

    # Play the game for NUM_ROUNDS rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)

        # Generate random numbers for the computer and the player
        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)

        print("Your number is", your_number)

        # Ask the player for their guess
        choice = input("Do you think your number is higher or lower than the computer's number? ").lower()

        # Validate the input until the player enters a valid option
        while choice not in ("higher", "lower", "high", "low"):
            choice = input("Please enter 'higher', 'lower', 'high', or 'low': ").lower()

        # Normalize input to standard form
        if choice == "high":
            choice = "higher"
        elif choice == "low":
            choice = "lower"

        # Check if the player's guess is correct
        higher_and_correct = choice == "higher" and your_number > computer_number
        lower_and_correct = choice == "lower" and your_number < computer_number

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_number)
            your_score += 1  # Increase score for correct guess
        else:
            print("That's incorrect. The computer's number was", computer_number)

        # Show current score
        print("Your score is now", your_score)
        print()

    # End of game summary
    print("Thanks for playing!")
    print("Your final score is", your_score)

    # Give feedback based on performance
    if your_score == NUM_ROUNDS:
        print("Perfect score! You're amazing!")
    elif your_score > NUM_ROUNDS // 2:
        print("Nice job, you played well!")
    else:
        print("Better luck next time!")

# Run the game only if this file is executed directly
if __name__ == "__main__":
    main()
