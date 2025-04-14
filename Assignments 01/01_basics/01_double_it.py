def main():
    # Ask the user to enter a number and convert it to an integer
    curr_value = int(input("Enter a number: "))

    # Keep doubling and printing the value until it is 100 or more
    while curr_value < 100:
        # Double the current value
        curr_value = curr_value * 2

        # Print the current value
        print(curr_value)

# Run the main function
if __name__ == "__main__":
    main()
