import curses
from curses import wrapper
from others import print_options

def main(scr):
  print(print_options()) # type: ignore
  

wrapper(main)
