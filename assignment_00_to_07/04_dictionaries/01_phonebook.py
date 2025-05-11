# A simple phonebook program that allows users to:
# 1. Store names and phone numbers
# 2. Display all entries in the phonebook
# 3. Look up specific phone numbers by name

def read_phone_numbers():
    """
    Reads names and phone numbers from user input until an empty name is entered.
    Returns:
        dict: A dictionary where keys are names and values are phone numbers
    """
    phonebook = {}
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Displays all entries in the phonebook in a formatted manner.
    Args:
        phonebook (dict): Dictionary containing name-number pairs
    """
    print("\n--- Phonebook ---")
    for name in phonebook:
        print(f"{name}'s contact number is {phonebook[name]}.")
    print("-----------------\n")

def lookup_numbers(phonebook):
    """
    Interactive function that allows users to look up phone numbers by name.
    Continues until user enters an empty name.
    Args:
        phonebook (dict): Dictionary containing name-number pairs
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"Sorry, no entry found for {name}.")
        else:
            print(f"{name}'s phone number is {phonebook[name]}.")

def main():
    """
    Main function that controls the program flow:
    1. Collects contact information
    2. Displays the complete phonebook
    3. Allows looking up individual numbers
    """
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
