def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    Assumes high is greater than low.
    """
    # Check if n is greater than or equal to low and less than or equal to high
    if low <= n <= high:
        return True
    # If the condition is not met, return False
    return False
def main():
    # Get input from user and convert to integers
    n = int(input("Enter the number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    # Call the in_range function and print the result
    if in_range(n, low, high):
        print(f"{n} is within the range [{low}, {high}].")
    else:
        print(f"{n} is not within the range [{low}, {high}].")

if __name__ == '__main__':
    main()
