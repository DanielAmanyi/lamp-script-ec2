def main():
    hr,mins = input(" What Time is it ? ").split(':')
    time = convert(hr,mins)

    if time >= 7.0 and time <= 8.0:
        print ("breakfast time")

    elif time >= 12.0 and time <= 13.0:
        print ("lunch time")

    elif time >= 18.0 and time <= 19.0:
        print ("dinner time")


def convert(x,z):
    y = x + '.'+ z
    return (float(y))





main()
