# Define voting age requirements for different countries
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    # Get the user's age as input
    user_age = int(input("\nHow old are you? "))

    # Check if the user can vote in Peturksbouipo (voting age: 16)
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"✅ You are eligible to vote in Peturksbouipo (Voting age: {PETURKSBOUIPO_AGE})")
    else:
        print(f"❌ You are not eligible to vote in Peturksbouipo (Voting age: {PETURKSBOUIPO_AGE})")

    # Check if the user can vote in Stanlau (voting age: 25)
    if user_age >= STANLAU_AGE:
        print(f"✅ You are eligible to vote in Stanlau (Voting age: {STANLAU_AGE})")
    else:
        print(f"❌ You are not eligible to vote in Stanlau (Voting age: {STANLAU_AGE})")

    # Check if the user can vote in Mayengua (voting age: 48)
    if user_age >= MAYENGUA_AGE:
        print(f"✅ You are eligible to vote in Mayengua (Voting age: {MAYENGUA_AGE})")
    else:
        print(f"❌ You are not eligible to vote in Mayengua (Voting age: {MAYENGUA_AGE})")

# Entry point of the program
if __name__ == '__main__':
    main()