def main():
    while True:
        fraction = prompt()
        if fraction != False:
            break
    # cnditions
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")
# input function
def prompt():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split('/')

            # Ensure x and y are both integers
            if not (x.isdigit() and y.isdigit()):
                raise ValueError

            # Convert x and y to integers
            x, y = int(x), int(y)

            # Ensure numerator is less than or equal to denominator
            if x > y:
                raise ValueError

            fraction = convert(x, y)
            return fraction
        except (ValueError, ZeroDivisionError):
            # Continue prompting in case of errors
            continue
# the Arithmetic Logic
def convert(x, y):
    num = (x / y) * 100
    return round(num)

main()
