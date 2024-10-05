import random


def get_level():
    level = 0
    while level < 1:
        try:
            level = int(input("Level: "))
            continue
        except ValueError:
            continue
    return level

def get_guess():
    guess = 0
    while guess < 1:
        try:
            guess = int(input("Guess: "))
            continue
        except ValueError:
            continue
    return guess





x = random.randint(1, level)
print("random:", x)

while guess > x:
    print("Too large!")
    guess = get_guess()

while guess < x:
    print("Too low!")
    level = get_level()



print("Just right!")



