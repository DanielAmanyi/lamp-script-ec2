x = 50
y = 0
z = 0
acceptable = [25,10,5]
while z <= 50:
    if z <= 50:
        y = int(input("Insert Coin "))
        if y in acceptable:
            z=y+z
            print("Amount Due:", x - z)
        if x <= z:
            print("Change Owed:", z -x)
            break
