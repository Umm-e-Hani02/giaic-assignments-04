# Define the adult age for the USA
ADULT_AGE = 18

# Function to check if a person is an adult
def is_adult(age: int):
    # If the person's age is greater than or equal to the adult age, return True
    if age >= ADULT_AGE:
        return True
    # Otherwise, return False
    return False

# Main function to interact with the user
def main():
    # Ask the user to input the person's age
    age = int(input("\033[1;3mHow old is the person? \033[0m"))
    # Call the is_adult function and print the result (True or False)
    print(is_adult(age))

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
