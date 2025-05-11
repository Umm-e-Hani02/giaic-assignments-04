import random

# Total number of rounds in the game
NUM_ROUNDS = 5

def main():
    score = 0  # Player's score starts at 0

    print("Welcome to HIGH-LOW game!")
    print("--------------------------")

    # Loop for each round
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")

        # Generate random numbers for computer and player
        computer_num = random.randint(1, 100)
        player_num = random.randint(1, 100)

        print(f"Your number is {player_num}")

        # Ask user for guess until valid input is given
        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if user_guess in ["higher", "lower"]:
                break
            print("Invalid input! Enter higher or lower.")

        # Check if the guess is correct and update score
        if user_guess == "higher" and player_num > computer_num:
            score += 1
            print(f"You are right! The computer's number is {computer_num}. Your score is now {score}.")
        elif user_guess == "lower" and player_num < computer_num:
            score += 1
            print(f"You are right! The computer's number is {computer_num}. Your score is now {score}.")
        else:
            print(f"Aww, that's incorrect. The computer's number is {computer_num}.")

    # Display final results after all rounds
    print("\nThanks for playing!")
    print(f"Your final score is {score} out of {NUM_ROUNDS}.")

    # Final message based on performance
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("You played really well.")
    else:
        print("Better luck next time.")

# Run the game
if __name__ == "__main__":
    main()
