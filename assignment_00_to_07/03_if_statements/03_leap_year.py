def main():
    # Get the year from user input
    year = int(input("Please enter a year to check if it's a leap year or not: "))

    # Leap year rules:
    # 1. Year must be divisible by 4
    # 2. If year is divisible by 100, it must also be divisible by 400
    if year % 4 == 0:
        # If divisible by 4, check if it's also divisible by 100
        if year % 100 == 0:
            # If divisible by 100, must also be divisible by 400 to be a leap year
            if year % 400 == 0:
                print(f"{year} is a leap year!")
            else:
                print(f"{year} is not a leap year.")
        else:
            # If divisible by 4 but not by 100, it's a leap year
            print(f"{year} is a leap year!")
    else:
        # If not divisible by 4, it's not a leap year
        print(f"{year} is not a leap year.")

# Entry point of the program
if __name__ == '__main__':
    main()