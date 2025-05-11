# Function to get the number of fruits in stock
def num_in_stock(fruit):
    # Dictionary containing stock data (all keys in lowercase)
    stock_data = {
        "apple": 200,
        "mango": 600,
        "banana": 350,
        "lychee": 500,
        "strawberry": 1000,
        "orange": 700
    }
    # Return stock for the given fruit (converted to lowercase)
    return stock_data.get(fruit.lower(), 0)

# Main function to run the program
def main():
    # Take fruit name as input with bold and italic styling
    fruit = input("\033[1;3mEnter fruit name: \033[0m")

    # Get stock count for the entered fruit
    stock = num_in_stock(fruit)

    # If fruit is available in stock
    if stock > 0:
        print(f"{fruit.capitalize()} is in stock. Here is how many:")
        print(stock)
    # If fruit is not available
    else:
        print(f"{fruit.capitalize()} is not in stock.")

# Run the main function
if __name__ == "__main__":
    main()
