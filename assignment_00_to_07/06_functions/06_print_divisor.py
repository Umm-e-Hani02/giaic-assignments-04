# Function to print all divisors of a number
def get_divisors(num: int):
    print(f"Here are the divisors of {num}:", end=" ")  # Print 

    for i in range(num):  # Loop from 0 to num - 1
        curr_divisor = i + 1  # Shift to 1-based indexing
        if num % curr_divisor == 0:  # Check if it's a divisor
            print(curr_divisor, end=" ")  # Print divisor in same line

# Main function
def main():
    num = int(input("\033[34mEnter a number: \033[0m"))  # Take number input from user
    get_divisors(num)  # Call function to get divisors

# Run main if this file is executed
if __name__ == "__main__":
    main()
