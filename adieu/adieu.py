import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        break

mylist = p.join((f"Adieu, adieu, to {names}"))
# mylist1 = p.join(("Liesl","Friedrich","Louisa"))
# "apple, banana, and carrot"

