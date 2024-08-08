# def payout(h):
    # twenty = "20"
    # if h in reward[h]:
    #     return twenty

# take in user input
greeting = input("Hi Customer! \n").strip().lower()

#logic to hunt for hello
if "hello" in greeting:
    print("0")

# logic to hunt for h
elif greeting[0] == "h":
    print("20")

# counter reaction
else:
    print("$100")
