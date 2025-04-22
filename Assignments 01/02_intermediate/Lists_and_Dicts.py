# Print the title of the program
print("Lists and Dicts")

# Create a list of fruits
my_list = ["apple", "mango", "orange", "pear", "peach"]

# Function to access an element at a given index
def access_element(my_list, index):
    """Returns the element at the specified index, or an error message if out of range."""
    if 0 <= index < len(my_list):
        return f'Element at index {index}: {my_list[index]}'
    return "Index out of range"

# Function to modify an element at a given index with a new value
def modify_element(my_list, index, new_value):
    """Modifies the element at the specified index with the new value."""
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f'Element at index {index} modified from {old_value} to {new_value}'
    return "Index out of range"

# Function to return a slice (sublist) from start index to end index (excluding end)
def slice_list(my_list, start, end):
    """Returns a new list containing the elements from the start index to the end index (exclusive)."""
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list):
        return f'Sliced list: {my_list[start:end]}'
    return "Invalid slice indices!"

# Function to print a welcome message when the game starts
def list_game():
    print("\nWelcome to the list manipulation game!")

# Re-define the fruit list to be used in the game
my_list = ["apple", "mango", "orange", "pear", "peach"]

# Start an infinite loop to keep the game running until the user chooses to quit
while True:
    # Show the current list
    print("Current list:", my_list)

    # Display menu options
    print("Select an operation:")
    print("1. Access Element")
    print("2. Modify Element")
    print("3. Slice List")
    print("4. Quit")

    # Ask the user to choose an operation
    choice = input("Enter your choice (1-4): ")

    # If user wants to access an element
    if choice == "1":
        index = int(input("Enter the index of the element you want to access: "))
        print(access_element(my_list, index))

    # If user wants to modify an element
    elif choice == "2":
        index = int(input("Enter the index of the element you want to modify: "))
        new_value = input("Enter the new value for the element: ")
        print(modify_element(my_list, index, new_value))

    # If user wants to slice the list
    elif choice == "3":
        start = int(input("Enter the start index for the slice: "))
        end = int(input("Enter the end index for the slice: "))
        print(slice_list(my_list, start, end))

    # If user wants to quit the game
    elif choice == "4":
        print("Exiting the game, thanks for playing.")
        break

    # If user enters an invalid option
    else:
        print("Invalid choice! Please enter a number between 1 to 4.")
        
if __name__ == "__main__":
    list_game()
