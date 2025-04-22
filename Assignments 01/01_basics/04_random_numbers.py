import random  # Import the random module to use random number functions

def main():
    # Print 10 random numbers from 1 to 100
    for i in range(10):
        number = random.randint(1, 100)  # Generate a random number between 1 and 100
        print(number, end=" ")  # Print the number on the same line, separated by a space

# Call the main function
if __name__ == "__main__":
    main()
