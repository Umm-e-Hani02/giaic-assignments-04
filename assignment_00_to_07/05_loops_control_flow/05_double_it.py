def main():
    # Ask the user to enter a number and convert it to an integer
    curr_value = int(input("Enter a number: "))

    # Continue multiplying the number by 2 while it's less than 100
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=" ")   # Print the updated value on the same line with a space

# This makes sure the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()
