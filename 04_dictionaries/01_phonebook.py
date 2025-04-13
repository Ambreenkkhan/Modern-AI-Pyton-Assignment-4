def read_phone_numbers():
    # This function collects names and phone numbers from the user.
    # It stores them in a dictionary called phonebook and returns it.
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            # Stop input if user presses Enter without typing a name
            break
        number = input("Number: ")
        phonebook[name] = number  # Add name-number pair to the phonebook

    return phonebook


def print_phonebook(phonebook):
    # This function prints all entries in the phonebook.
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_numbers(phonebook):
    # This function allows the user to search for a number by entering a name.
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            # Stop lookup if user presses Enter without typing a name
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook")
        else:
            print(f"{name}'s number is {phonebook[name]}")


def main():
    # This is the main driver function that calls all other functions
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


if __name__ == '__main__':
    main()
