import curses
from curses import wrapper

def main(stdscr):
  stdscr.clear()
  stdscr.refresh()
  stdscr.addstr("Welcome Player")
  stdscr.getch()
wrapper(main)