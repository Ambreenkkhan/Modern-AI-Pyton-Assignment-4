# Constants used in the program
PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Why do programmers prefer dark mode? Because the light attracts bugs!"
SORRY = "Sorry, I only tell jokes."

def main():
    # Ask the user what they want
    user_input = input(PROMPT)

    # Check if the user asked for a joke
    if user_input == "Joke":
        print(JOKE)
    else:
        # Any other input will result in the sorry message
        print(SORRY)

if __name__ == "__main__":
    main()
