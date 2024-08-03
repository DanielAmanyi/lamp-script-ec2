def smile(char):
    char =  char.replace(":)", "\U0001F642")
    return char

def fire(char):
    char = char.replace(":fire:", "\U0001F525")
    return char

def love(char):
    char = char.replace("<3", "\U00002764")
    return char

def confused(char):
    char = char.replace(":/" | ":-/", "\U0001F615")
    return char

def sad(char):
    char = char.replace(":(", "\U0001F641")
    return char


# Take in user input
user_input = input ("your favorite smiley character: ")


#Run logic
if ":)" in user_input:
    print(smile(user_input ))

elif ":(" in user_input:
    print(sad(user_input))

elif ":/" in user_input:
    print(confused())

elif "<3" in user_input:
    print(love(user_input))

elif ":fire:" in user_input:
    print(fire(user_input))
