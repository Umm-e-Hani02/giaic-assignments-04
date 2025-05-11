# This program creates a list by continuously asking the user for input values
# until they enter an empty value (just press Enter)

def main():
    # Initialize an empty list to store user inputs
    list = []

    # Get the first value from the user
    val = input("Enter a value: ")
    
    # Continue asking for values until the user enters an empty value
    while val:
        # Add the current value to the list
        list.append(val)
        # Ask for the next value
        val = input("Enter a value: ")

    # Display the final list to the user
    print(f"Here's the list {list}")

# This ensures the main function only runs if this file is executed directly
if __name__ == "__main__":
    main()