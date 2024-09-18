items = []
while True:
    try:
        item = input().upper()
        items.append(item)
    except EOFError:
        items.sort()
        # Using a dictionary to count occurrences
        count_dict = {}
        for name in items:
            if name in count_dict:
                count_dict[name] += 1
            else:
                count_dict[name] = 1
        # Print each unique item with its count
        for name in sorted(count_dict.keys()):
            counter = count_dict[name]
            print(f"{counter} {name}", end="\n")
        break
