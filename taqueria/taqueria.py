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
        #    print(f"Total: ${menu[i]}")
           return menu[i]


def get_total(item):
    for i in new_menu:
        if i in menu:
            bill.append(menu[i])
        else:
            get_input()
            break
    print(f"Total: ${sum(bill):.2f}")

# list(menu)
def get_input():
    while True:
        try:
            item =input("Item:  ").title()
            new_menu.append(item)
            item = get_item()
            # continue

        except EOFError:
            # print(end="")
            get_total(item)
            # print()
            break
        # except ValueError:
        #     return False

get_input()

