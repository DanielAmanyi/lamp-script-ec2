def insert_(i):
    i = ("_"+i).lower()
    return i


camel_case = input("Enter Name ")
for i in camel_case:
    if i.isupper():
        i = insert_(i)
    print(i,end="")
print()
