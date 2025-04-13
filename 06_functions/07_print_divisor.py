def print_divisors(num: int):
  # Function to print all divisors of a given number
    print(f"Here are the divisors of {num}:")
    
    # Loop through numbers from 1 to num (inclusive)
    for i in range(num):
        checked_divisor  = i + 1  # Current number to check for divisibility
        if num % checked_divisor  == 0:  # Check if it divides num evenly
            print(checked_divisor )  # Print the divisor

def main():
    # Get input from the user and convert it to an integer
    num = int(input("Enter a number: "))
    
    # Call the function to print all divisors of the entered number
    print_divisors(num)

if __name__ == '__main__':
    main()
