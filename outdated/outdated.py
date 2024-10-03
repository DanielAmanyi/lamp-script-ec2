import re

# List of months
calendar = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Convert Month String to int
def get_month_number(month):
    for index, name in enumerate(calendar, start=1):
        if month.capitalize() == name:
            return index
    return None  # If the month is not found

# Function to validate and parse the date
def parse_date(date):
    # Check if the date is in MM/DD/YYYY format
    numeric_pattern = r"^\s*(\d{1,2})/(\d{1,2})/(\d{4})\s*$"
    match = re.match(numeric_pattern, date)

    if match:
        month, day, year = match.groups()
        month, day, year = int(month), int(day), int(year)

        # Validate month and day range
        if 1 <= month <= 12 and 1 <= day <= 31:
            return year, month, day

    # Check if the date is in "Month Day, Year" format
    written_pattern = r"^\s*([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})\s*$"
    match = re.match(written_pattern, date)

    if match:
        month_str, day, year = match.groups()
        month = get_month_number(month_str)
        day, year = int(day), int(year)

        # Validate month and day range
        if month and 1 <= day <= 31:
            return year, month, day

    return None  # Invalid date format

while True:
    date_input = input("Enter Date (e.g., 11/9/2022 or September 8, 1636): ")
    parsed_date = parse_date(date_input)

    if parsed_date:
        year, month, day = parsed_date
        print(f"{year}-{month:02d}-{day:02d}")
        break
    else:
        print("Invalid date format. Please try again.")
