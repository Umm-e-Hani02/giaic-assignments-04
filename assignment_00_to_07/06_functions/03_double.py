# This function takes a number and returns its double
def double(num):
    return num * 2  # Multiply the number by 2 and return it

# The main function where the program starts
def main():
    num = int(input("\033[1;3mEnter a number: \033[0m"))  # Ask the user to enter a number and convert it to an integer
    double_num = double(num)  # Call the double function to get twice the value of the entered number
    print(f"The double of {num} is {double_num}.")  # Print the result in a formatted message

# This ensures the main() function runs only if the file is executed directly
if __name__ == "__main__":
    main()
