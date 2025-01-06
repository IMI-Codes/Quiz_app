#immediate test of functions
import curses 
from curses import wrapper
from main import print_text

def test(scr):
  print_text(scr,"Hello")
  scr.getch()
  
wrapper(test)