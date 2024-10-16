# def payout(h):
    # twenty = "20"
    # if h in reward[h]:
    #     return twenty


def main():
    # take in user input
    while True:
        try:
            greeting = input("Hi Customer! \n").strip().lower()
            print(value(greeting))
            break
        except ValueError:
            continue




def value(greeting):
    # logic to hunt for hello
    if "hello" in greeting:
        return("$0")

    # logic to hunt for h
    elif greeting[0] == "h":
        return("$20")

    # counter reaction
    else:
        return("$100")


if __name__ == "__main__":
    main()
