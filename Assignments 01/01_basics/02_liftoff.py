def main():
    # Loop from 10 down to 1 
    # range(start, stop, step) - we use step = -1 to count down
    for i in range(10, 0, -1):
        print(i, end=" ")  # Print the number with a space, stay on the same line

    # After the countdown ends, print "Liftoff!"
    print("Liftoff!")

# Run the main function
if __name__ == "__main__":
    main()
