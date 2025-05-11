# import random module to genrate random numbers
import random

# Defining the number of sides on each die
NUM_SIDES = 6

def main():

     # randint(1, NUM_SIDES) generates a number between 1 and 6
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    # Calculate the sum of both dice rolls
    total: int = die1 + die2

    # Display the results to the user
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice {total}")

# Call the main function
if __name__ == '__main__':
    main()