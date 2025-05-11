# This program generates a specified number of random integers within a given range
# and prints them to the console.

import random

# Constants defining the parameters for random number generation
TOTAL_NUMBERS : int = 10  # Number of random numbers to generate
MIN_VALUE : int = 1       # Minimum value for random numbers
MAX_VALUE : int = 100     # Maximum value for random numbers

def main():
    """
    Main function that generates and prints random numbers.
    It generates TOTAL_NUMBERS random integers between MIN_VALUE and MAX_VALUE
    and prints them to the console with a space between each number.
    """
    for _ in range(TOTAL_NUMBERS):
        random_num = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_num, end=' ')  # Print each number with a space, not a newline

if __name__ == '__main__':
    main()