import sys
from pyfiglet import Figlet
f = Figlet(font='slant')

text = input("Input: ")
if sys.argv == 2:
    print ("output:",f.renderText(text))
elif sys.argv == 0:
    print("output:",renderText(text))
