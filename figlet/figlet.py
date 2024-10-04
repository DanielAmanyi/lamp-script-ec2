import sys
from pyfiglet import Figlet
f = Figlet(font='slant')


# elif sys.argv == 0:
text = input("Input: ")
print("output:",Figlet(text))

if sys.argv == 2:
    text = input("Input: ")
    print ("output:",f.renderText(text))

