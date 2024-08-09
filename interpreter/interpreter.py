
result = input("enter your arithmetic: ")
x,y,z = result.split()

def add(x,y):
    return x+y

def sub(x,y):
    return x - y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y


if y == '+':
    result = add(int(x),int(z))
    print(float(result))

if y == '-':
    result = sub(int(x),int(z))
    print(float(result))

if y == '/':
    result = div(int(x),int(z))
    print(float(result))

if y == '*':
    result = mult(int(x),int(z))
    print(float(result))
