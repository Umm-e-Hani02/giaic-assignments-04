INCHES_IN_FOOT  = 12 # 1 feet = 12 inches

def main():

    # User Input
    feet: float = float(input("Enter length in feet: "))

    # Formula of conversion
    inches: float = feet * INCHES_IN_FOOT

    # Result
    print(f"{feet} feet = {inches} inches")

# Call the main function
if __name__ == '__main__':
    main()