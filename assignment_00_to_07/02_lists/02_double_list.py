# This program demonstrates how to double each element in a list
def main():
    # Initialize a list of integers
    numbers: list[int] = [1,2,3,4]

    # Iterate through each index in the list
    for i in range(len(numbers)):
        # Get the element at the current index
        elem_index = numbers[i]
        # Double the element and store it back at the same index
        numbers[i] = elem_index * 2

    # Print the modified list with all elements doubled
    print(numbers)

# Call the main function
if __name__ == "__main__":
    main()