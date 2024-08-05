def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}\n")

def dollars_to_float(d):
    # Convert the dollar input to a float and return it
    return float(d.replace('$', ''))

def percent_to_float(p):
    # Convert the percentage input to a float, divide by 100, and return it
    return float(p.replace('%', '')) / 100

main()
