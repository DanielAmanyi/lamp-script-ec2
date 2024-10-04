import sys
from pyfiglet import Figlet
f = Figlet(font='slant')
g = Figlet()


# elif sys.argv == 0:

# text = input("Input: ")
# print("output:",g.renderText(text))


for i in sys.argv:
    if sys.argv == 2:
        text = input("Input: ")
        print ("output:",f.renderText(text))

