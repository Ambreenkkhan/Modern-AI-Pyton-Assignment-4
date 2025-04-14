def main():
    # Prompt the user to enter their name and store it in the variable 'name'
    name: str = input("What's your name? ")
    
    # Call the greet() function with the user's name and print the returned greeting
    print(greet(name))

# Function to generate a greeting message for the given name
def greet(name):
    return f"{name}! 🤲 May Allah bless your life with joy, health, and endless success."  # return a personalized greeting

if __name__ == '__main__':
    main()
