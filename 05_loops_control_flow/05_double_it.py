def main():
    # Ask user to enter a number and convert it to an integer
    curr_value = int(input("Enter a number: "))

    # Keep doubling and printing the value until it reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=" ")   # Print the new value on the same line with space

if __name__ == "__main__":
    main()
