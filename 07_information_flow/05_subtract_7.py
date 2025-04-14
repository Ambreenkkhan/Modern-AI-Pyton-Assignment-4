def subtract_seven(num):# Helper function to subtract 7 from the given number
    return num - 7  # Subtract 7 and return the result

def main(): # Main function
    # Ask the user to enter a number
    user_input = int(input("Enter a number: "))
    
    # Call the subtract_seven function with the user input
    result = subtract_seven(user_input)
    
    # Print the result
    print(f"Result after subtracting 7 - {user_input} = {result}")

if __name__ == "__main__":
    main()
