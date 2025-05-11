# This function counts how many even numbers are in the given list
def count_even(lst):
    count = 0  # Initialize a counter to keep track of even numbers
    for num in lst:  # Loop through each number in the list
        if num % 2 == 0:  # Check if the number is even (divisible by 2)
            count += 1  # If it's even, increase the counter by 1

    # Print the total number of even numbers found in the list
    print(f"There are {count} even numbers in the list.")

# This function gets a list of integers from the user
def get_ints():
    lst = []  # Create an empty list to store user input
    user_input = input("Enter an integer or press enter to stop: ")  # Ask for the first input
    while user_input != "":  # Keep asking until the user just presses Enter without typing anything
        lst.append(int(user_input))  # Convert input to integer and add it to the list
        user_input = input("Enter an integer or press enter to stop: ")  # Ask again

    return lst  # Return the complete list of entered integers

# The main function that coordinates the process
def main():
    lst = get_ints()  # Get the list of integers from the user
    count_even(lst)  # Count and print how many of those numbers are even

# This checks if the script is being run directly (not imported)
if __name__ == '__main__':
    main()  # Run the main function
