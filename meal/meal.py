def convert(hours_str, minutes_str):
    # Convert hours and minutes to float
    hours = float(hours_str)
    minutes = float(minutes_str)

    # Convert minutes to a fraction of an hour and return total hours
    return hours + minutes / 60.0

def main():
    # Prompt user for time input in HH:MM format
    time_input = input("What Time is it? (in HH:MM format) ")

    try:
        # Split input into hours and minutes
        hr, mins = time_input.split(':')

        # Convert to decimal hours
        time = convert(hr, mins)

        # Determine and print meal time based on the converted time
        if 7.0 <= time < 8.0:
            print("Breakfast time")
        elif 12.0 <= time < 13.0:
            print("Lunch time")
        elif 18.0 <= time < 19.0:
            print("Dinner time")
        else:
            print("Not meal time")

    except ValueError:
        print("Invalid time format. Please use HH:MM format.")

# Run the main function
main()
