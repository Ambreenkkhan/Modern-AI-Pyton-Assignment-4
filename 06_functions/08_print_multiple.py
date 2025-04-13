def print_multiple(message: str, repeats: int):
    # Function to print a message multiple times
    for i in range(repeats):  # Loop from 0 to repeats - 1
        print(message)  # Print the message
def main():
    # Ask the user to enter a message
    message = input("Please type a message: ")

    # Ask the user how many times to repeat the message
    repeats = int(input("Enter the number of times to repeat your message: "))

    # Call the function to print the message multiple times
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
