import curses

DEFAULT_OPTIONS = ["YES","NO"]

curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
highlighter = curses.color_pair(1)