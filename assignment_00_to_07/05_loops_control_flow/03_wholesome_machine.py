# A constant affirmation string that the user needs to type exactly
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    # Print the instruction for the user
    print(f"Please type the following affirmation: {AFFIRMATION}")

    # Start an infinite loop to repeatedly ask the user until they get it right
    while True:

        # Prompt the user to input text in blue color (using ANSI escape code \033[34m)
        user_input = input("\033[34m")
        
        # Reset the color back to normal after input
        print("\033[0m", end="")

        # Check if the user input matches the affirmation exactly
        if user_input == AFFIRMATION:
            print("That's right! :)")  # Correct input message
            break  # Exit the loop
        else:
            # If input doesn't match, prompt again with the full affirmation
            print("That's not correct. Please type the following affirmation:", AFFIRMATION)

# This ensures that main() runs when the script is executed directly
if __name__ == '__main__':
    main()
