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
if guess > random.randrange(level+1):
    print("Too large!")
elif guess < random.randrange(level+1):
    print("Too low!")
else:
    print("Just righ!")

