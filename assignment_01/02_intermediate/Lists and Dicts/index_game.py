# Function to access an element from the list at a specific index
def access_elements(lst, index):
    if 0 <= index < len(lst):  # Check if index is valid
        return lst[index]
    else:
        return "Index out of range"

# Function to modify an element at a specific index
def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):  # Check if index is valid
        lst[index] = new_value
        return lst
    else:
        return "Index out of range"

# Function to return a slice from the list
def slice_list(lst, start_index, end_index):
    return lst[start_index:end_index]  # Slicing doesn't raise error even if out of range

# Main function to run the program
def main():
    lst = [1, 2, 3, 4, 5]  # Example list
    print(f"Current list: {lst}")
    print("Choose an operation:\n1. access (to view an item)\n2. modify (to change an item)\n3. slice (to get part of the list)")
    
    operation = input("Enter operation (access/modify/slice): ").lower()  # Convert input to lowercase

    if operation == "access":
        index = int(input("Enter index to access: "))  # Ask for index
        print(access_elements(lst, index))

    elif operation == "modify":
        index = int(input("Enter index to modify: "))  # Ask for index
        new_value = input("Enter new value: ")  # Ask for new value
        print(modify_element(lst, index, new_value))

    elif operation == "slice":
        start_index = int(input("Enter start index: "))  # Ask for starting index
        end_index = int(input("Enter end index: "))      # Ask for ending index
        print(slice_list(lst, start_index, end_index))

    else:
        print("Invalid operation.")  # Handle wrong input

# Run the main function
if __name__ == "__main__":
    main()
