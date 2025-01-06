import curses
from typing import Optional
def print_text(win,text:str,pos:Optional[tuple]=None):
  win.addstr(0,0,text)#this works