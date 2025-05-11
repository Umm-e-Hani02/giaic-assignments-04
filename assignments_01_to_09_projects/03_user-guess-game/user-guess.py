import random

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 10.")
print("Can you guess what it is?\n")

# Computer selects a random number
secret_number = random.randint(1, 10)
attempts = 10

# User keeps guessing until they get it right
while attempts > 0:
    guess = int(input("Enter your guess: "))
    attempts -= 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed it right!")
        print(f"It took you {10 - attempts} attempts.")
        break

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
