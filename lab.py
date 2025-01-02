import curses
from curses import wrapper



def print_menu(win,menu,row):
   curses.curs_set(0)
   curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
   highlighter = curses.color_pair(1)
   win.clear()
   for idx, row in enumerate(menu):
    if idx == row:
      win.addstr(idx, 0, row,highlighter)
    else:
      win.addstr(idx, 0, row)
      win.refresh()
   
   while True:
     key = win.getch()
     if key == curses.KEY_UP and row > 0:
       row -= 1
     elif key == curses.KEY_DOWN and row < len(menu) - 1:
          row += 1
     elif key == curses.KEY_ENTER or key in [10, 13]:
        win.addstr(len(menu) + 1, 0, f"You selected '{menu[row]}'!")
        win.refresh()
        win.getch()

       
     
     
      
def main(scr):
  
  options = ["1","2","3","4","5"]
  current_row:int = 0
  print_menu(scr,options,current_row)
  
 

wrapper(main)