AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    # Display the affirmation that user needs to type exactly
    print("Please type the following affirmation: " + AFFIRMATION)

    # Take input from the user
    user_feedback = input()

    # Keep asking until user types the exact affirmation
    while user_feedback != AFFIRMATION:
        # Inform the user their input was incorrect
        print("That was not the affirmation.")

        # Ask again for the correct affirmation
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    # User typed the correct affirmation
    print("That's right! :)")

if __name__ == '__main__':
    main()
