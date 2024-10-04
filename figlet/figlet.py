import sys
from pyfiglet import Figlet
f = Figlet(font='slant')


if sys.argv == 2:
    text = input("Input: ")
    print ("output:",f.renderText(text))
elif sys.argv == 0:
    text = input("Input: ")
    print("output:",renderText(text))
