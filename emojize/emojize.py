import emoji

english_text = input("Input: ")
names = emoji.emojize(english_text)
print(f"Output: {names}",language='alias')


# print(emoji.emojize('Python is :thumbs_up:'))
