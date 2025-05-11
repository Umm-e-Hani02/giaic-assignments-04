C = 299792458  # Speed Of Light (m/s)

def main():
    print("\n--- Mass to Energy Converter ---")

    # User Input
    mass_in_kg: float = float(input("\n\033[1;3mEnter mass in Kilogram(kg): \033[0m"))

    # Formula of conversion
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Result
    print("\n--- Result ---")
    print(f"Given Mass: {mass_in_kg}kg")
    print(f"Speed of Light: {C}m/s")
    print(f"Energy: {energy_in_joules} joules\n")

# Call the main function
if __name__ == '__main__':
    main()
