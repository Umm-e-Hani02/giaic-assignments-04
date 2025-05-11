import random  # Importing the random module to use random number generation

DONE_LIKEHOOD = 0.4  # There's a 40% chance that the done() function will return True
# (Note: There's a typo here. It should be DONE_LIKELIHOOD instead of DONE_LIKEHOOD)

# This function randomly decides whether to stop counting or not
def done():
    return random.random() < DONE_LIKEHOOD  # Generates a random number between 0.0 and 1.0

# This function counts from 1 to 10, but might stop early if done() returns True
def chaotic_counting():
    for i in range(1, 11):  # Loop from 1 to 10
        if done():          # Check if we should stop counting
            return          # If yes, exit the function immediately
        print(i, end=" ")   # Otherwise, print the number with a space

# This is the main function that starts the program
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Start the chaotic counting
    print("\nI'm done.")  # This line prints when chaotic_counting() is finished

# This ensures that the main function runs only when the file is executed directly
if __name__ == "__main__":
    main()
