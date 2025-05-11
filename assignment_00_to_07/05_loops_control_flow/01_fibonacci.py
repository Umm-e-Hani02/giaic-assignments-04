MAX_VALUE = 10000  # Constant value to limit the Fibonacci sequence

def main():
    # Initial values for the Fibonacci sequence
    curr_value = 0  # First Fibonacci number
    next_value = 1  # Second Fibonacci number

    # While loop to generate Fibonacci sequence as long as current value is less than MAX_VALUE
    while curr_value < MAX_VALUE:
        print(curr_value)  # Print the current Fibonacci number

        # Calculate the next number in the Fibonacci sequence
        value_after_next = curr_value + next_value
        
        # Update the current value and next value for the next iteration
        curr_value = next_value  # Move to the next number in the sequence
        next_value = value_after_next  # Set the new next number for the next iteration

# This ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
