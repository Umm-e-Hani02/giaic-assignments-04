import random

def main():
    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)

    # Prompt the user to guess the number
    print("I am thinking of a number between 1-99")
    user_input = int(input("Guess the number: "))

    # Keep asking until the guess is correct
    while user_input != secret_number:
        if user_input < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        # Ask for a new guess
        user_input = int(input("Enter a new number: "))

    # Congratulate the user when the guess is correct
    print(f"Congrats! Your guess is right. The number was {secret_number}")

if __name__ == "__main__":
    main()
