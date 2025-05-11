# Function to subtract 7 from the given number
def subtract_seven(num):
    return num - 7

def main():
    # Take number input from the user
    num = int(input("Enter a number: "))
    
    # Call the function to subtract 7
    result = subtract_seven(num)
    
    # Print the result
    print(f"Result after deleting 7: {result}")

# Run the main function
if __name__ == "__main__":
    main()
