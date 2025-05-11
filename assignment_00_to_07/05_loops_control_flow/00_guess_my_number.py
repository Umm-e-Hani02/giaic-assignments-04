import random  # Importing the random module to generate a random number

def main():
    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)
    print("\nI am thinking of a number between 1 and 99...")
    print("Type q for quit the game anytime.\n")

    # Start an infinite loop until the correct guess is made
    while True:

        user_input = input("Enter a guess: ")

        if user_input == "q":
            print("👋 Game exited. Thanks for playing!")
            break
        try:
            guess = int(user_input)

            # Check if the guess is outside the valid range
            if guess < 1 or guess > 99:
                print("Please enter a number between 1 and 99.")

            # If the guess is lower than the secret number
            elif guess < secret_number:
                print("Your guess is too low.")

            # If the guess is higher than the secret number
            elif guess > secret_number:
                print("Your guess is too high.")

            # If the guess is correct
            else:
                print(f"🎉 Congrats! The number was: {secret_number}")
                break  # Exit the loop

        except ValueError:
            # Handle the case when the user enters something that's not a number
            print("⚠️ Please enter a valid number.")


# This line makes sure the game runs when the script is executed
if __name__ == '__main__':
    main()
