import random

def computer_guess(x):
    print(f"Think of a number between 1 and {x} and I will try to guess it.")
    
    # Set the initial low and high range
    low = 1
    high = x
    
    # Loop until the computer guesses correctly
    while True:
        # Computer makes a guess
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")
        
        # Ask for feedback
        feedback = input("Is my guess too High (H), too Low (L), or Correct (C)? ").lower()
        
        if feedback == 'c':  # If the guess is correct
            print(f"Yay! I guessed your number {guess} correctly!")
            break
        elif feedback == 'h':  # If the guess is too high
            high = guess - 1
        elif feedback == 'l':  # If the guess is too low
            low = guess + 1
        else:
            print("Please enter a valid input: 'H', 'L', or 'C'.")

# Play the game with a range of 1 to 20
computer_guess(20)
