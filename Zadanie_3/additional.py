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
        os.system('clear')          # Clearing console for Linux and macOS operating systems.
    else:
        os.system('cls')            # Clearing console for Windows operating system.


"""
    @ Function: press_to_continue()
    
    @ Parameters: None
    
    @ Description: function mainly used to halt program execution, so that user may read what is being
    displayed in console terminal
"""


def press_to_continue():
    input("Naciśnij dowolny klawisz aby kontynuować...")


"""
    @ Function: read_function_args()
    
    @ Parameters:
    
    * file_name -> name of the file, where the arguments of a certain function will be read from
    
    @ Description: this method is used to retrieve arguments for a certain function, and they are used
    to calculate interpolated function's values.
"""


def read_function_args(file_name):
    list_of_args = []
    file = open(file_name, "r")
    for line in file:
        line.replace('\n', '')
        list_of_numbers = line.split(';')
        for number in list_of_numbers:
            list_of_args.append(float(number))
    return list_of_args