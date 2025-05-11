import random

# Constants for the number of random values and the range
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate and print 10 random numbers between 1 and 100 on the same line
    for _ in range(N_NUMBERS):
        random_nums = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_nums, end=" ")  # Print numbers with space instead of newline

if __name__ == "__main__":
    main()
