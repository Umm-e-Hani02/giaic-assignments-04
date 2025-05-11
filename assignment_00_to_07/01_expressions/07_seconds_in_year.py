# Constants for time conversion
DAYS_PER_YEAR = 365
HOURS_PER_DAY_ = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

# Calculate total seconds in a year using multiplication
# Formula: days × hours × minutes × seconds
total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY_ * MIN_PER_HOUR * SEC_PER_MIN

def main():

    # Print the result in a nice formatted way
    print(f"There are {total_seconds} seconds in year!")

# Call the main function
if __name__ == '__main__':
    main()