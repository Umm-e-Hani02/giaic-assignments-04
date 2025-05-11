MINIMUM_HEIGHT : int = 4  # Minimum height in feet (equivalent to 50 inches)

def main():
    # Get the user's height in feet
    height = float(input("How tall are you? Please enter your height in feet: "))

    # Check if the user is tall enough to ride
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to enjoy the ride! 🎢")
    else:
        print("Sorry, you're not tall enough to ride this time. But maybe next year! 😊")

# Entry point of the program
if __name__ == '__main__':
    main()
