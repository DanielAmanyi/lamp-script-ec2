def main():
    # Take in user input
    while True:
        greeting = input("Hi Customer! \n").strip().lower()
        # Ensure greeting is not empty
        if greeting:
            print(value(greeting))
            break
        else:
            print("Please enter a valid greeting.")  # Prompt for valid input

def value(greeting):
    # Logic to hunt for "hello"
    if "hello" in greeting:
        return "$0"

    # Logic to hunt for words starting with "h"
    elif greeting[0] == "h":
        return "$20"

    # Counter reaction for all other cases
    else:
        return "$100"

if __name__ == "__main__":
    main()
