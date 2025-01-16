import curses
from typing import Optional


def print_options(area:str,options:list):
  curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
  #going to assume the first row 0 is occupied hence starting from 1
  #also consider adding the row to start from as a argument and refactor based on that
  
  curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
  current_row = 1
  for id,value in options:
    area.addstr(id+1,0,value) # type: ignore
    if current_row == id:
      area.addstr(id+1,0,value,curses.color_pair(1)) # type: ignore
"""
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

for idx,value in enumerate(options):
        if current_row == idx:
          area.addstr(idx+1,0,value,curses.color_pair(1))
        else:
          area.addstr(idx+1,0,value)
    while True:
      key = area.getch()
      #logic for selection
 """    



""" def print_text(win,text:str,pos:Optional[tuple]=None):
  win.addstr(0,0,text)#this works """