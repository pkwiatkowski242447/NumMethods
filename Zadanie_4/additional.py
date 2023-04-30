import os

"""
    @ Function: print_new_line()

    @ Parameters: None

    @ Description: this function is used for printing a new line on the console terminal.
"""


def print_new_line():
    print('')


"""
    @ Function: clear_screen()

    @ Parameters: None

    @ Description: function used for clearing console terminal in any operating system (of course
    the method to clear the screen depends on the OS.)
"""


def clear_screen():
    if os.name == 'posix':
        os.system('clear')  # Clearing console for Linux and macOS operating systems.
    else:
        os.system('cls')  # Clearing console for Windows operating system.


"""
    @ Function: press_to_continue()

    @ Parameters: None

    @ Description: function mainly used to halt program execution, so that user may read what is being
    displayed in console terminal
"""


def press_to_continue():
    input("Naciśnij dowolny klawisz aby kontynuować...")