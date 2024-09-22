items = {}

items = {}

def update_db(item):
    if item in items:
        items[item] += 1  # Increment count if item already exists
    else:
        items[item] = 1  # Initialize count for a new item
    return

while True:
    try:
        item = input("").upper()  # Take input and convert to uppercase
        update_db(item)  # Update the items dictionary

    except EOFError:
        # Sort items and print them in the required format
        for item in sorted(items):
            print(f"{items[item]} {item}")
        break

