def get_user_data(): # Function to get user data
    # Ask the user for their first name and store it in a variable
    first_name = input("What is your first name?: ")
        # Ask the user for their last name and store it in a variable
    last_name = input("What is your last name?: ")
        # Ask the user for their email address and store it in a variable
    email = input("What is your email address?: ")
        # Return all the collected data as a tuple
    return first_name, last_name, email

def main(): # Main function to display the received data
    # Call get_user_data() to collect the user's information
    user_data = get_user_data()
    
    # Print the received user data
    print(f"Received the following user data: {user_data}")

if __name__ == "__main__":
    main()
