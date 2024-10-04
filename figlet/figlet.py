import sys
from pyfiglet import Figlet
f = Figlet(font='slant')
g = Figlet()



# Default Prompt
for i in sys.argv:
    if len(sys.argv) == 1:
        text = input("Input: ")
        print("output:",g.renderText(text))
        break


# Scan for Command Line Argument
for i in sys.argv:
    if len(sys.argv) == 3:
        text = input("Input: ")
        print ("output:",f.renderText(text))
        break

