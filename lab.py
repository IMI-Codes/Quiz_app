import curses
from curses import wrapper


def print_menu(win,menu,row):
   curses.start_color()
   curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
   win.clear()
   for idx, row in enumerate(menu):
    if idx == row:
      win.addstr(idx, 0, row, curses.color_pair(1))
    else:
      win.addstr(idx, 0, row)
      win.refresh()
      
def main(scr):
  options = ["1","2","3","4","5"]
  current_row = 0
  print_menu(scr,options,current_row)
  scr.getch()

wrapper(main)