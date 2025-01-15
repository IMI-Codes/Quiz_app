import curses
from curses import wrapper
from typing import Optional

def main(win):
  win.clear()
  win.addstr(0,0,"Welcome Player")
  player_statuses = ["New Player","Existing Player"]
  
  def print_options(area,options:list,message:Optional[str]=None):
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_MAGENTA)
    current_row = 0
    if message:
      area.clear()
      area.addstr(0,0,message)
    else:
      pass #Come back to this use case
      
    
  print_options(win,player_statuses,"Please Pick One")
  #win.getch()
wrapper(main)
""" 

for idx,value in enumerate(options):
        if current_row == idx:
          area.addstr(idx+1,0,value,curses.color_pair(1))
        else:
          area.addstr(idx+1,0,value)
    while True:
      key = area.getch()
      #logic for selection
 """    