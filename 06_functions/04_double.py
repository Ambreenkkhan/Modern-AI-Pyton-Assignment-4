def double(num):
    # Returns the result of multiplying the input number by 2
    return num * 2  # Perform the multiplication and return the result

def main():
    user_input = input("Enter a number: ")  # Prompt the user to enter a number
    num = int(user_input)  # Convert the input string to an integer
    result = double(num)  # Get the double of the number using the double() function
    print("Double that is", result)  # Print the final result

if __name__ == "__main__":
    main() 
