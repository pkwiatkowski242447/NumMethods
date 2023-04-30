import additional as ad


def print_main_menu():
    print("===== Zadanie 4 - Całkowanie numeryczne =====")
    print("1. Całkowanie przy wykorzystaniu kwadratury Newtona - Cotesa.")
    print("1. Całkowanie przy wykorzystaniu kwadratury Gaussa.")
    print("3. Zakończenie działania programu")
    print("=============================================")


def function_choice_menu():
    print("===== Wybór funkcji do przeprowadzenia całkowania =====")
    print("1. (0.2 x - 1.2) / sqrt(1 - x ^ 2)")
    print("2. (0.7 |x| - 2) / sqrt(1 - x ^ 2)")
    print("3. sin(x) / sqrt(1 - x ^ 2)")
    print("4. (x ^ 3 - 3 x ^ 2 - 1) / sqrt(1 - x ^ 2)")
    print("5. (sin(x) ^ 3 - 2 |cos(x)|) / sqrt(1 - x ^ 2)")
    print("6. Powrót do poprzedniego menu")
    print("=======================================================")


def print_newton_cotes_menu():
    choice = 0
    while choice != "6":
        ad.clear_screen()
        function_choice_menu()
        choice = input("Podaj twój wybór: ")
        epsilon_value = float(input("Podaj dokładność wyznaczenia wartość całki oznaczonej:"))


def print_gauss_menu():
    choice = 0
    while choice != "6":
        ad.clear_screen()
        function_choice_menu()
        choice = input("Podaj twój wybór: ")
        epsilon_value = float(input("Podaj dokładność wyznaczenia wartość całki oznaczonej:"))