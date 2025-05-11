# Import math module for mathematical operations like square root
import math

def main():
    # Get the length of first side (AB) from user
    # Convert string input to float number for calculations
    ab: float = float(input("Enter the length of AB: "))

    # Get the length of second side (AC) from user
    # Convert string input to float number for calculations
    ac: float = float(input("Enter the length of AC: "))

    # Calculate hypotenuse using Pythagorean theorem
    # Formula: c = √(a² + b²) where c is hypotenuse
    bc = math.sqrt(ab**2 + ac**2)

    # Display the result (length of hypotenuse BC)
    print(f"The length of BC (the hypotenuse) is: {bc}")
    
# Call the main function
if __name__ == '__main__':
    main()