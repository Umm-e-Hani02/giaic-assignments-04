def main():
    # Prompt the user to enter a number and convert it to an integer
    curr_value = int(input("Enter a number: "))

    # Continuously double the value until it reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == "__main__":
    main()
