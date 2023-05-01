import additional as ad
import calc as cl


def print_main_menu():
    print("===== Zadanie 4 - Całkowanie numeryczne =====")
    print("1. Całkowanie przy wykorzystaniu kwadratury Newtona - Cotesa.")
    print("2. Całkowanie przy wykorzystaniu kwadratury Gaussa.")
    print("3. Zakończenie działania programu")
    print("=============================================")


def function_choice_menu():
    print("===== Wybór funkcji do przeprowadzenia całkowania =====")
    print("1.  (0.2 x - 1.2) / sqrt(1 - x ^ 2)")
    print("2.  (0.7 |x| - 2) / sqrt(1 - x ^ 2)")
    print("3.  sin(x) / sqrt(1 - x ^ 2)")
    print("4.  (x ^ 3 - 3 x ^ 2 - 1) / sqrt(1 - x ^ 2)")
    print("5.  (sin(x) ^ 3 - 2 |cos(x)|) / sqrt(1 - x ^ 2)")
    print("6.  (2 ^ x) / sqrt(1 - x ^ 2)")
    print("7.  (sin(7x + 6)) / sqrt(1 - x ^ 2)")
    print("8.  ((sin 2x) ^ 3 - 1) / sqrt(1 - x ^ 2)")
    print("9.  (|x| ^ 3 - 2 * |x| + 8) / sqrt(1 - x ^ 2)")
    print("10. (8.1 sin(x) + x) / sqrt(1 - x ^ 2)")
    print("=======================================================")


def print_newton_cotes_menu():
    choice = 0
    while True:
        ad.clear_screen()
        function_choice_menu()
        choice = input("Podaj twój wybór: ")
        if 1 <= int(choice) <= 10:
            ad.print_new_line()
            epsilon_value = float(input("Podaj dokładność wyznaczenia wartość całki oznaczonej: "))
            return cl.get_limit_value_for_newton_cotes(choice, epsilon_value)
        else:
            ad.print_new_line()
            print("Wybierz numer funkcji z menu!")
            ad.press_to_continue()


def print_gauss_menu():
    choice = 0
    while True:
        ad.clear_screen()
        function_choice_menu()
        choice = input("Podaj twój wybór: ")
        if 1 <= int(choice) <= 10:
            ad.print_new_line()
            number_of_nodes = int(input("Podaj liczbę węzłów, na której zostanie przeprowadzone całkowanie: "))
            return cl.calculate_definite_integral_gauss(choice, number_of_nodes)
        else:
            ad.print_new_line()
            print("Wybierz numer funkcji z menu")
            ad.press_to_continue()