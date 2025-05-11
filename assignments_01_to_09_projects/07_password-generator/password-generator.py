import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    # Create an empty pool of characters
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Check if at least one option is selected
    if not characters:
        return "⚠️ Please select at least one character type."

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User Input
print("Welcome to the Password Generator!")
length = int(input("Enter the length of the password: "))
use_uppercase = input("Include UPPERCASE letters? (y/n): ").lower() == "y"
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

# Generate and display the password
password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
print("\nGenerated Password: ", password)
