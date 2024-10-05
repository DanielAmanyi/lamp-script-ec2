import inflect
p = inflect.engine()


while True:
    try:
        name = input("Name: ")


    except: 
mylist = p.join(("apple", "banana"))
mylist1 = p.join(("Liesl","Friedrich","Louisa"))
# "apple, banana, and carrot"
print(mylist1)
