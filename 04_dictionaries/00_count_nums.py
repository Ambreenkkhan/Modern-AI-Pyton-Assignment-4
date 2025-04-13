def get_user_numbers():
    # This function takes numbers from the user until an empty input is entered.
    # It stores the numbers in a list and returns it.
    user_numbers = []
    
    while True:
        user_input = input("Enter a number: ")

        if user_input == "":
            # Stop taking input when the user enters an empty string.
            break

        # Convert the input to an integer
        num = int(user_input)

        # Add the number to the list
        user_numbers.append(num)

    return user_numbers


def count_nums(num_lst):
    # This function takes a list of numbers and returns a dictionary
    # with each number as a key and its count as the value.
    
    num_dict = {}

    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1  # First time the number is seen
        else:
            num_dict[num] += 1  # Increment count if number already exists

    return num_dict


def print_counts(num_dict):
    # This function prints how many times each number appeared
    # using f-strings for better formatting.

    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")


def main():
    # Main function to run the steps in order.
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# Python boilerplate: 
if __name__ == '__main__':
    main()
