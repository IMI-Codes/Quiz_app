import curses

def display_menu(stdscr, options):
    # Initialize curses and hide the cursor
    curses.curs_set(0)
    
    # Index to track the selected option
    current_row = 0

    def print_menu():
        stdscr.clear()
        for idx, option in enumerate(options):
            if idx == current_row:
                stdscr.addstr(idx, 0, option, curses.color_pair(1))  # Highlight selected
            else:
                stdscr.addstr(idx, 0, option)
        stdscr.refresh()

    # Set up color pairs for highlighting
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Main loop to handle user input
    while True:
        print_menu()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, 10, 13]:  # Enter key pressed
            return options[current_row]

# Wrapper function to call the display_menu with curses
def main():
    options = ["Option 1", "Option 2", "Option 3", "Option 4", "Exit"]
    selected_option = curses.wrapper(display_menu, options)
    print(f"You selected: {selected_option}")

if __name__ == "__main__":
    main()
