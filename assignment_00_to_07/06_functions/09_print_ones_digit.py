# Function to print the ones digit of a number
def print_ones_digit(num):
    print(f"The ones digit is {num % 10}")  # Extract and print the last digit using modulo operator

# Main function
def main():
    # Ask user to enter a number (text in blue color)
    num = int(input("\033[34mEnter a number: \033[0m"))  
    print_ones_digit(num)  # Call the function to display ones digit

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
