def convert(time_str):
    """
    Convert a time string in HH:MM format to a float representing the time in hours.

    :param time_str: Time in HH:MM format (e.g., "7:30" or "13:45")
    :return: Time as a float (e.g., 7.5 or 13.75)
    """
    # Split the time string into hours and minutes
    hours_str, minutes_str = time_str.split(':')

    # Convert hours and minutes to float
    hours = float(hours_str)
    minutes = float(minutes_str)

    # Convert minutes to a fraction of an hour and return total hours
    return hours + minutes / 60.0

def main():
    """
    Main function to prompt the user for a time and determine if it's breakfast, lunch, or dinner time.
    """
    # Prompt user for time input in HH:MM format
    time_input = input("What Time is it? (in HH:MM format) ")

    try:
        # Convert time to decimal hours
        time = convert(time_input)

        # Determine and print meal time based on the converted time
        if 7.0 <= time <= 8.0:
            print("Breakfast time")
        elif 12.0 <= time <= 13.0:
            print("Lunch time")
        elif 18.0 <= time <= 19.0:
            print("Dinner time")
        # If time does not fall within any meal time ranges, do nothing

    except ValueError:
        print("Invalid time format. Please use HH:MM format.")

# Run the main function
if __name__ == "__main__":
    main()
