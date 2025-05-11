# Function to print a message multiple times
def print_multiple(message: str, repeat: int):
    for i in range(repeat):  # Repeat the loop 'repeats' times
        print(message)  # Print the message

# Main function
def main():
    message = input("\033[34mPlease type a message: \033[0m")  # Take message input from user
    repeat = int(input("\033[34mEnter a number of times to repeat your message: \033[0m"))  # Take how many times to repeat
    print_multiple(message, repeat)  # Call function to print message

# Run main if this file is the main program
if __name__ == "__main__":
    main()
