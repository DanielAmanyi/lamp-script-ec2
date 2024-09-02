menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
new_menu = []
bill = []
def get_item():
    for i in new_menu:
        if i in menu:
            bill.append(menu[i])
    print(f"\nTotal: ${sum(bill):.2f}")


# list(menu)

while True:
    try:
        item =input("Item:  ").title()
        new_menu.append(item)
    except EOFError:
        get_item()
        break

