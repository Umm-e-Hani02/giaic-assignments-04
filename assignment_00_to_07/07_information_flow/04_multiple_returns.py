# Function to get user information from input
def get_user_info():
    # Ask for user's first name
    first_name = input("Enter first name: ")
    # Ask for user's last name
    last_name = input("Enter last name: ")
    # Ask for user's email address
    email = input("Enter your email address: ")

    # Return all collected data as a tuple
    return first_name, last_name, email

# Main function to handle the flow
def main():
    # Get user data from input function
    user_data = get_user_info()
    
    # Print the collected user data
    print(f"Received the following user data: {user_data}")

# Entry point of the program
if __name__ == "__main__":
    main()
