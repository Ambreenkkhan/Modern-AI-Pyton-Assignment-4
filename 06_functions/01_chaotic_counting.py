import random

# Set the likelihood that the counting will stop
DONE_LIKELIHOOD = 0.3  # 30% chance that counting will stop at each iteration

# Function to perform chaotic counting
def chaotic_counting():
    # Loop through numbers 1 to 10
    for i in range(10):
        current_number = i + 1  # Calculate the current number to print
        # Check if the done() function returns True (chance to stop)
        if done():
            return  # Exit the function if the done() function returns True
        print(current_number, end=" ")  # Print the current number on the same line with a space

# Function that determines whether we should stop based on random chance
def done():
    """Returns True with a probability of DONE_LIKELIHOOD"""
    if random.random() < DONE_LIKELIHOOD:  # Compare random value with DONE_LIKELIHOOD
        return True  # Stop counting if random value is less than DONE_LIKELIHOOD
    return False  # Continue if random value is greater than DONE_LIKELIHOOD

# Main function that runs the program
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Start the chaotic counting function
    print("I'm done")  # Print this when counting is complete or stopped

if __name__ == "__main__":
    main()
