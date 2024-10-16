# Vowels Library
def main():
    # Take in user input
    tweet = input("Enter your tweet: ")
    # Convert tweet to a list
    tweet = list(tweet)
    print(shorten(tweet))


def shorten(tweet):
    tweet = list(tweet)  # Convert string to list
    vowels = "aeiouAEIOU"

    for char in tweet[:]:  # Iterate over a copy to avoid skipping
        if char in vowels:
            tweet.remove(char)  # Remove the vowel

    return ''.join(tweet)  # Convert back to string



if __name__ == "__main__":
    main()
