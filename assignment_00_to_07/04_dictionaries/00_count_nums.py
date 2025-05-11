# Function to get numbers from the user until they press Enter
def get_user_numbers():
    user_number = []

    while True:
        # Prompt user to enter a number or press Enter to stop
        user_input = input("\033[94mEnter a number or press enter to stop: \033[0m")

        if user_input == "":
            break  # Stop taking input if user presses Enter without typing a number

        num = int(user_input)  # Convert input to integer
        user_number.append(num)  # Add the number to the list

    return user_number  # Return the list of numbers


# Function to count the frequency of each number in the list
def count_nums(num_lst):
    num_dict = {}

    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1  # First time this number appears
        else:
            num_dict[num] += 1  # Increment count if number already exists

    return num_dict  # Return the dictionary with frequencies


# Function to print how many times each number appears
def print_counts(num_dict):
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")


# Main function to run the whole program
def main():
    user_numbers = get_user_numbers()      # Step 1: Get user input numbers
    num_dict = count_nums(user_numbers)    # Step 2: Count each number's frequency
    print_counts(num_dict)                 # Step 3: Display the results


# Call main() only when this file is run directly
if __name__ == '__main__':
    main()
