# Vowels Library
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Take in user input
tweet = input("Enter your tweet: ")

# Convert tweet to a list
tweet = list(tweet)

# Loop through each character in the tweet
for i in tweet[:]:
    if i in vowels:
        tweet.remove(i)  # Remove the vowel

# Convert the list back into a string and print the result
print(''.join(tweet), end="")
