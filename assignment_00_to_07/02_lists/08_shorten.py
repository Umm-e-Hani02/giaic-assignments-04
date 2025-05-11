# This program demonstrates list manipulation by shortening a list to a maximum length
# The commented-out code at the top shows an alternative implementation that was previously used

# Note: Previous implementation is commented out (lines 1-18)

# Maximum allowed length for the list
MAX_LENGTH = 3

def shorten(my_list):
    """
    Shortens a list to the MAX_LENGTH by removing elements from the end
    and printing each removed element.
    
    Args:
        my_list: The list to be shortened
    """
    while len(my_list) > MAX_LENGTH:
        # Remove and store the last element of the list
        last_elem = my_list.pop()
        # Print the removed element
        print(last_elem)

def get_list():
    # Initialize an empty list to store user inputs
    my_list = []
    
    # Get the first element from the user
    elem = input("Please enter an element of the list or press enter to stop. ")
    
    # Continue asking for elements until user enters an empty string
    while elem != "":
        my_list.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")

    return my_list

def main():
    """
    Main function that:
    1. Gets a list from user input
    2. Shortens the list to MAX_LENGTH elements
    """
    my_list = get_list()
    shorten(my_list)

# Entry point of the program
if __name__ == "__main__":
    main()
