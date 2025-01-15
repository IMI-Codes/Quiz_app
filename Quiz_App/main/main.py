import curses
from curses import wrapper
from typing import Optional

def main(win):
  win.clear()
  win.addstr(0,0,"Welcome Player")
  player_statuses = ["New Player","Existing Player"]
  
  def print_options(area,options:list,message:Optional[str]=None):
    
    if message:
      area.clear()
      
      for idx,value in enumerate(options):
        area.addstr(idx+1,0,value)
    else:
      pass
    
  print_options(win,player_statuses,"What")
  win.getch()
wrapper(main)