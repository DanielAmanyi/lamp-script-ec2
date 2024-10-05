import random

while True:
    try:
        level = int(input("Level: "))
        guess = int(input("Guess: "))

    except ValueError:
        continue
    
