items = []
while True:
    try:
        item = input("").upper()
        items.append(item)
    except EOFError:
        items.sort()
        for names in items:
            counter = items.count(names)
            print(counter, names)
        break
