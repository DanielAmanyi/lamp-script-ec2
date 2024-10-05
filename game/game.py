import random
level = 0
guess = 0

while level < 1 or guess < 1:
    try:
        level = int(input("Level: "))
        guess = int(input("Guess: "))
    except ValueError:
        continue
if guess > random.randint(level)
