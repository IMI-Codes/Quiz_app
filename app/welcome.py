import curses
from curses import wrapper


def main(scr):
  curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_YELLOW)
  BLUE_YELLOW = curses.color_pair(1)
  scr.clear()
  scr.refresh()
  scr.addstr(0,50,"WELCOME PLAYER",BLUE_YELLOW | curses.A_BOLD)#curse.A_bold
  scr.getch()

wrapper(main)