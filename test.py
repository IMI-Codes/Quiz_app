import curses
from curses import wrapper


#from passlib.hash import pbkdf2_sha256

import curses

def main(stdscr):
    # Disable cursor and enable keypad input
    curses.curs_set(0)
    stdscr.keypad(1)
    
    # Define menu options
    menu = ["Option 1", "Option 2", "Option 3", "Exit"]
    current_row = 0

    def print_menu(stdscr, selected_row):
        stdscr.clear()
        for idx, row in enumerate(menu):
            if idx == selected_row:
                stdscr.addstr(idx, 0, row, curses.color_pair(1))
            else:
                stdscr.addstr(idx, 0, row)
        stdscr.refresh()

    # Set up color pair for selected menu item
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    print_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[current_row] == "Exit":
                break
            stdscr.addstr(len(menu) + 1, 0, f"You selected '{menu[current_row]}'!")
            stdscr.refresh()
            stdscr.getch()

        print_menu(stdscr, current_row)

curses.wrapper(main)
