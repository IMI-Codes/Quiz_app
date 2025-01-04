import curses
from constants import highlighter

def print_options(win,options):
  curses.curs_set(0)
  current_row = 0
  
  def print_menu():
    win.clear()
    for idx, option in enumerate(options): # type: ignore
      if idx == current_row:
        win.addstr(idx,0,option,highlighter)
      else:
        win.addstr(idx,0,option)
    win.refresh()
    
  while True:
    print_menu()
    key = win.getch()
    if key == curses.KEY_UP and current_row > 0:
      current_row -= 1
    elif key == curses.KEY_DOWN and current_row < len(options) - 1:
      current_row += 1
    elif key in [curses.KEY_ENTER, 10, 13]:  # Enter key pressed
      return options[current_row]