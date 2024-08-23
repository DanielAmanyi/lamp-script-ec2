def main():
    plate = input("Enter Plate Number: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length of plate
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that the plate starts with at least two letters
    if not s[0:2].isalpha():
        return False

    #Check for special characters (#*&^&$ etc)
    if not s.isalnum():
        return False

    # Check the position of numbers
    for i in range(len(s)):
        if s[i].isdigit():
            # check for numbers ending
            if not s[i:].isdigit():
                return False
            # First number cannot be '0'
            if s[i] == '0':
                return False
            break

    return True


main()
