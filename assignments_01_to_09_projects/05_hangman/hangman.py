import random

# Word list
words = [
    "repository", "inspiration", "coding", "dedication", "grateful",
    "intelligence", "designer", "software", "programming", "learning"
]

def hangman():
    word = random.choice(words)  # Get a random word
    guessed_word = ["_"] * len(word)  # Create a list with "_" for each letter in the word
    tries = 0
    max_tries = 6

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))

    while tries < max_tries:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():  # Input validation
            print("Please enter a valid letter.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Good job! " + " ".join(guessed_word))
        else:
            tries += 1
            print(f"Wrong guess! You have {max_tries - tries} tries left.")

        if "_" not in guessed_word:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"You lost! The word was: {word}")

# Start the game
hangman()
