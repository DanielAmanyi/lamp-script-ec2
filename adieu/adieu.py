import inflect
p = inflect.engine()


mylist = p.join(("apple", "banana"))
mylist1 = p.join(("Liesl","Friedrich","Louisa"))
# "apple, banana, and carrot"
print(mylist1)
