# Function to add three copies of the given data to a list
def add_three_copies(list, data):
    # Loop three times to append the data
    for i in range(3):
        list.append(data)

def main():
    # Initialize an empty list
    list = []
    # Get user input for the message to be copied
    message = input("Enter a message to copy: ")
    # Display the list before adding copies
    print(f"List before: {list}")
    # Call function to add three copies of the message
    add_three_copies(list, message)
    # Display the list after adding copies
    print(f"List after: {list}")
    
# Execute the main function if this file is run directly
if __name__ == '__main__':
    main()