def count_even(lst):
    # This function counts and prints how many even numbers are present in the given list.
    # >>> count_even([1, 2, 3, 4])
    # 2
    # >>> count_even([1, 3, 5, 7])
    # 0
  
    count = 0  # Variable to store how many even numbers we find

    # Looping over the list using indexing (instead of directly iterating over elements)
    for i in range(len(lst)):
        num = lst[i]  # Get the element at index i
        if num % 2 == 0:  # Check if the number is even
            count += 1  # Increase the count if it's even

    print(count)  # Display the total count of even numbers

def get_list_of_ints():#This function collects integers from the user until they press enter.
    # It returns the complete list of integers entered.
    lst = []  # Empty list to store user-entered integers
    user_input = input("Enter an integer or press enter to stop: ")  # Ask for input
    while user_input != "":  # Keep asking until input is empty
        lst.append(int(user_input))  # Convert the input to an integer and add to list
        user_input = input("Enter an integer or press enter to stop: ")  # Ask again

    return lst  # Return the complete list

def main(): # Main function to run the program.
    
    # Gets a list of integers from the user and prints the count of even numbers.
    
    lst = get_list_of_ints()  # Call function to get user input
    count_even(lst)  # Count and print even numbers from the list

if __name__ == '__main__':
    main()
