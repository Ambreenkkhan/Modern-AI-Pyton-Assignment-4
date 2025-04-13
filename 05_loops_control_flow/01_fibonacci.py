MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0      # Start of the Fibonacci sequence
    next_term = 1      # The next number in the sequence

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)  # Print the current Fibonacci number

        # Calculate the next Fibonacci number
        term_after_next = curr_term + next_term

        # Move to the next terms in the sequence
        curr_term = next_term
        next_term = term_after_next

if __name__ == '__main__':
    main()
