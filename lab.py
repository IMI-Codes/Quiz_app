import curses 
from curses import wrapper
def display_menu(win,menu):
  curses.curs_set(0)
  current_row = 0
  
  def print_menu():
    win.clear()
    for idx,option in enumerate(menu):
       if idx == current_row:
          win.addstr(idx, 0, option, curses.color_pair(1))  # Highlight selected
       else: 
          win.addstr(idx, 0, option)
          win.refresh()
  curses.start_color()
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

  while True:
      print_menu()

      key = win.getch()

      if key == curses.KEY_UP and current_row > 0:
          current_row -= 1
      elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
          current_row += 1
      elif key in [curses.KEY_ENTER, 10, 13]:  # Enter key pressed
          return menu[current_row]


def main(scr):
  pass
  


wrapper(main)
