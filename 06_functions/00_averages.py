def get_average(x: float, y: float):
    # Returns the average value between two given numbers
    return (x + y) / 2

def main():
    # Calculate the average of 5 and 15
    first_avg = get_average(5, 15)

    # Calculate the average of 12 and 18
    second_avg = get_average(12, 18)

    # Now average the two results above
    combined_avg = get_average(first_avg, second_avg)

    # Display all average results
    print("First Average:", first_avg)
    print("Second Average:", second_avg)
    print("Combined Average:", combined_avg)

# Start the program
if __name__ == '__main__':
    main()
