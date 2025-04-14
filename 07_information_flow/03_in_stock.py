# Function to check the number of fruits in stock
def num_in_stock(fruit):
    inventory = {
        "apple": 50,
        "banana": 120,
        "pear": 1000,
        "orange": 75
    }
    # Return the number of the fruit in stock if it exists, otherwise return 0
    return inventory.get(fruit.lower(), 0)

# Main function
def main():
    # Ask the user to enter a fruit
    fruit = input("Enter a fruit: ")
    # Get the number of that fruit in stock
    stock = num_in_stock(fruit)

    # Check if the fruit is in stock or not
    if stock > 0:
        print("This fruit is in stock! Here is how many:\n")
        print(stock)
    else:
        print("This fruit is not in stock.")


# Call main function
if __name__ == "__main__":
    main()
