def main():
    # Dictionary containing gravity factors for each planet
    planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Get weight from user (as integer)
    weight_on_earth = int(input("Enter a weight on Earth: "))

    # Get planet name from user and capitalize first letter
    planet = input("Enter a planet: ")

    # Check if planet is in dictionary
    if planet in planet_gravity:
        # Calculate weight on the selected planet
        weight_on_planet = round(weight_on_earth * planet_gravity[planet], 2)
        print(f"The equivalent weight on {planet}: {weight_on_planet}")
    else:
        # Error message for invalid planet
        print("Invalid planet name. Please enter a valid planet from the solar system.")

# Call main function
if __name__ == "__main__":
    main()
