import random
level = 0
guess = 0

while level < 1 or guess < 1:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        else:
            break
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        else:
            break
    except ValueError:
        continue


