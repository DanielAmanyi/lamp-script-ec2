import sys
from pyfiglet import Figlet
f = Figlet(font='slant')
if sys.argv == 2:
    print (f.renderText(sys.argv[1]))
