# Constant to define the legal adult age, in this case for the U.S. (18 years old)
ADULT_AGE: int = 18  

def is_adult(age: int) -> bool:
    """
    Checks if a person is an adult based on the given age.

    Parameters:
    age (int): The age of the person to check.

    Returns:
    bool: True if the person is an adult (age >= 18), otherwise False.
    """
    if age >= ADULT_AGE:
        return True  # The person is an adult
    return False  # The person is not an adult

def main():
    """
    Main function that prompts the user for an age and prints if the person is an adult.
    """
    try:
        # Get input from the user, and ensure it's converted to an integer
        age: int = int(input("How old is this person?: "))
        
        # Check if the person is an adult and print the result
        print(is_adult(age))
    
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Please enter a valid number for the age.")

if __name__ == "__main__":
    main() 
