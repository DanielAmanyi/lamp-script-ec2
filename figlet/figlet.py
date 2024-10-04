import sys
from pyfiglet import Figlet
f = Figlet(font='slant')
g = Figlet()


# elif sys.argv == 0:

text = input("Input: ")
print("output:",g.renderText(text))

# prompt = sys.argv
for i in sys.argv:
    if len(sys.argv) == 3:
        text = input("Input: ")
        print ("output:",f.renderText(text))

