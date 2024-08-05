def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float(dollars) * float(percent)
    print(f"Leave ${tip:.2f} \n")


def dollars_to_float(d):
    # TODO
    float(d)
    return d


def percent_to_float(p):
    # TODO
    p = float(p)/100
    return float(p)


main()
