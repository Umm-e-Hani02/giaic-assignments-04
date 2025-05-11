def main():

    # Get the numbers we want to divide
    dividend: int = int(input("\033[1;3mEnter the number to divide: \033[0m"))  # The number being divided
    divisor: int = int(input("\033[1;3mEnter the number to divide by: \033[0m"))  # The number to divide by

    # Perform integer division and get remainder
    quotient = dividend // divisor  # Integer division (no decimals)
    remainder = dividend % divisor  # Modulus operator gives the remainder

    # Display the result
    print(f"The result is {quotient} with {remainder} remainder")
# Call the main function
if __name__ == '__main__':
    main()