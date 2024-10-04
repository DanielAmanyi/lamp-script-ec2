import sys
from pyfiglet import Figlet
f = Figlet(font='slant')
g = Figlet()



# Default Prompt
text = input("Input: ")
print("output:",g.renderText(text))


# Scan for Command Line Argument
for i in sys.argv:
    if len(sys.argv) == 3:
        text = input("Input: ")
        print ("output:",f.renderText(text))

