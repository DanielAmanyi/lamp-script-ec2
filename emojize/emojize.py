import emoji

english_text = input("Input: ")
names = emoji.emojize(english_text,language='alias')
print(f"Output: {names}")
# print(emoji.emojize('Python is :thumbsup:', language='alias'))

# print(emoji.emojize('Python is :thumbs_up:'))
