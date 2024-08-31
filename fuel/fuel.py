
def main():
    while True:
        fraction = prompt()
        if fraction != False:
            break

    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")

def prompt():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split('/')
            fraction = convert(x, y)
            return fraction
        except (ValueError, ZeroDivisionError):
            # Go back to the prompt if there's an error
            continue

def convert(x, y):
    num = float(x) / float(y)
    num = num * 100
    return num

main()
