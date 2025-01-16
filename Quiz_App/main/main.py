import curses
from curses import wrapper
from typing import Optional
from utils.helpers.main import print_options
def main(win):
  win.clear()
  win.addstr(0,0,"Welcome Player")
  player_statuses = ["New Player","Existing Player"]
  win.addstr(2,0,"Please Any Key")
  #Quiz_App
  
  
wrapper(main)
