import random

NUM_SIDES = 6  # Total sides on each die

def roll_dice():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Die 1 rolled: {die1}, Die 2 rolled: {die2}, Total: {total}")

def main():
    die1: int = 10  # Local variable in main

    print(f"\ndie1 in main() starts as: {die1}\n")

    for i in range(1, 4):
        print(f"Roll {i}:")
        roll_dice()
        print()  # Empty line for better spacing

    print(f"die1 in main() is still {die1}")

# Call the main function
if __name__ == '__main__':
    main()
