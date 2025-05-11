import random

# Function to get the computer's choice
def computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

print("Welcome to Rock, Paper, Scissors!")

# Main game loop
while True:
    user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()

    if user_choice not in ['rock', 'paper', 'scissor']:
        print("Invalid input! Please choose rock, paper, or scissor.")
        continue

    computer = computer_choice()
    print(f"Computer chose: {computer}")

    # Decide the winner
    if user_choice == computer:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer == 'scissor') or \
         (user_choice == 'paper' and computer == 'rock') or \
         (user_choice == 'scissor' and computer == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
