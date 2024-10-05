import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        break

mylist = p.join(("apple", "banana"))
mylist1 = p.join(("Liesl","Friedrich","Louisa"))
# "apple, banana, and carrot"
print(mylist1)
