def print_ones_digit(num: int):
    """
    Prints the ones digit of the given integer.

    Parameters:
    num (int): The number from which the ones digit will be extracted.
    """
    ones_digit = num % 10  # Use modulo to get the ones digit (remainder when divided by 10)
    print(f"The ones digit is {ones_digit}")  # Print the ones digit
def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))  
    # Call the function to print the ones digit of the number
    print_ones_digit(num)

if __name__ == "__main__":
    main() 
