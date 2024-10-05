import random
level = 0
guess = 0

while level < 1 or guess < 1:
    try:
        level = int(input("Level: "))
        guess = int(input("Guess: "))
        break
    except ValueError:
        continue
if guess > random.randint(level):
    print("Too large!")
elif guess < randomrandint(level):
    print("Too low!")
else:
    print("Just righ!")

