# This program simulates a fruit shop where users can purchase different fruits
# and calculates their total bill based on the quantities selected

# Dictionary containing fruit prices in dollars
# Each fruit is a key with its corresponding price as the value
fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}

def main():
    """
    Main function that runs the fruit shop program:
    1. Iterates through available fruits
    2. Asks user for quantity of each fruit
    3. Calculates and displays total price
    """
    # Initialize total price counter to keep track of the bill
    total_price = 0

    # Loop through each fruit and its price in the dictionary
    # items() returns both key (fruit_name) and value (price)
    for fruit_name, price in fruits.items():
        # Get user input for quantity of each fruit
        # Using ANSI escape codes for bold and italic text formatting
        # \033[1;3m starts bold and italic formatting
        # \033[0m resets the formatting
        fruit_amount = int(
            input(f"\n\033[1;3mHow many {fruit_name}s would you like to purchase?: \033[0m"))
        
        # Calculate cost for current fruit (price * quantity) and add to total
        total_price += (price * fruit_amount)

    # Display final bill with 2 decimal places for cents
    # Using emoji 🛒 for visual appeal
    print(
        f"\n🛒 The total cost of your fruits is: ${total_price:.2f}\nThank you for shopping with us!")


# Python boilerplate to ensure main() only runs if this file is run directly
if __name__ == '__main__':
    main()
