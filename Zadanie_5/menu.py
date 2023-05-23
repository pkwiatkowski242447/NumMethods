"""
    @ Function: print_main_menu()

    @ Parameters: None

    @ Returns: void

    @ Description: The main goal of this function's existance is to print main menu of the program - that is
    two option for user to chose from - first one, that offers approximation of some function and second, which
    is responsible for terminating the program.
"""


def print_main_menu():
    print("========== Zadanie 5 - Aproksymacja ==========")
    print("1. Wybór funkcji do aproksymacji.")
    print("2. Zakończenie działania programu.")
    print("==============================================")


"""
    @ Function: function_choice_menu()

    @ Parameters: None

    @ Returns: void

    @ Description: This method is used for displaying menu with available function, for user to choose from in
    order to approximate them.
"""


def function_choice_menu():
    print("======= Wybór funkcji do aproksymacji =======")
    print("1.  f(x) = 0.6 x - 1.3")
    print("2.  f(x) = 2.1 |x| - 3.0")
    print("3.  f(x) = 3 sin(2x) - 0.5")
    print("4.  f(x) = x ^ 3 - 3 x ^ 2 + x - 7")
    print("5.  f(x) = |x| ^ 3 - 3 |x| ^ 2 + |x| - 7")
    print("6.  f(x) = 1.5 cos(|2x|) - 0.25")
    print("7.  f(x) = 0.75 |sin(0.5 x)|")
    print("8.  f(x) = sin(2x) ^ 3 - 3 sin(2x) ^ 2 + sin(2x) - 7")
    print("9.  f(x) = sin(x) + 2x - 5")
    print("10. f(x) = 2.1 * sin(x ^ 3 - 3 x ^ 2 + x - 7)")
    print("11. f(x) = 2 * sin(3x) + cos(3x)")
    print("12. f(x) = x ^ 3 + cos(x)")
    print("==============================================")


"""
    @ Function: program_mode_menu()

    @ Parameters: None

    @ Returns: void

    @ Description: This function is used in order to let user choose program function, that is: if polynomial degree
    will be entered by the user or integration error value. 
"""


def program_mode_menu():
    print("========= Wybór trybu pracy programu =========")
    print("1. Podawanie stopnia wielomianu aproksymującego.")
    print("2. Podawanie oczekiwanego błędu aproksymacji.")
    print("==============================================")


def variant_choice_menu():
    print("=== Wybór typu wielomianów do aproksymacji ===")
    print("1. Wielomiany Czebyszewa")
    print("2. Wielomiany Hermite'a")
    print("3. Wielomiany Laguerra'a")
    print("4. Wielomiany Legendre'a")
    print("==============================================")
