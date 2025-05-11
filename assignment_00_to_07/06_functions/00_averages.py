# This function calculates the average of two numbers
def average(num1, num2):
    return (num1 + num2) / 2  # Add the two numbers and divide by 2

def main():
    # Take first number input from the user and convert it to float
    num1 = float(input("Enter a number: "))

    # Take second number input from the user and convert it to float
    num2 = float(input("Enter another number: "))

    # Call the average function and display the result using f-string
    print(f"The average of {num1} and {num2} is {average(num1, num2)}")

# This makes sure the main function runs only when this file is run directly
if __name__ == '__main__':
    main()
