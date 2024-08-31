
def main():
    while True:
        fraction = prompt()
        if fraction != False:
            break
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")

def prompt():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split('/')
            if fraction <= 1:
                print("E")

            # Ensure x and y are both integers
            if not (x.isdigit() and y.isdigit()):
                raise ValueError

            fraction = convert(x, y)
            return fraction
        except (ValueError, ZeroDivisionError):
            # Continue prompting in case of errors
            continue

def convert(x, y):
    num = float(x) / float(y)
    num = num * 100
    return round(num)

main()
