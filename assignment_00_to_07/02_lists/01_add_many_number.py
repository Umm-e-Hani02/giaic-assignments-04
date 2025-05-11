# This function takes a list of numbers and returns their sum
def add_numbers(numbers)->int:
    # Initialize the total with starting value of 0
    total_so_far:int = 0
    # Loop through each number in the list and add it to the total
    for number in numbers:
        total_so_far += number

    # Return the final sum
    return total_so_far

# Main function where the program execution begins
def main():
    # Create a list of numbers from 1 to 5
    numbers: list[int] = [1,2,3,4,5]
    # Calculate the sum by calling add_numbers function with our list
    total_sum = add_numbers(numbers)
    # Print the final result
    print(f"Total sum = {total_sum}")

# Call the main function
if __name__ == "__main__":
    main()