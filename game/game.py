import random
level = 0
guess = 0
while True:
    if level or guess < 1:
        try:
            level = int(input("Level: "))
            guess = int(input("Guess: "))
            break
        except ValueError:
            continue
    else:
        break

