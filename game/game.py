import random
level = 0
guess = 0

while level < 1:
    try:
        level = int(input("Level: "))
        continue
    except ValueError:
        continue

while guess < 1:
    try:
        guess = int(input("Guess: "))
        continue
    except ValueError:
        continue





x = random.randint(1,level)
print(x)
if guess > x:
    print("Too large!")
elif guess < x:
    print("Too low!")
else:
    print("Just right!")



