import curses
from curses import wrapper
from others import *

def main(scr):
  print(print_options()) # type: ignore
  

wrapper(main)
