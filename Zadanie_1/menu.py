def print_menu():
    print("===== Menu =====")
    print("1. Wybór funkcji do wyznaczenia miejsc zerowych i wyświetlenia.")
    print("2. Zakończenie działania programu")
    print("================")


def chose_functions():
    print("===== Wybór funkcji od wyświetlenia i wyznaczenia miejsc zerowych =====")
    print("1. x ^ 3 + 2 * x ^ 2 + 7")
    print("2. cos(x)")
    print("3. e ^ x - x ^ 4")
    print("4. (cos(x)) ^ 3 + 2 * (cos(x)) ^ 2 + 7 - x ^ 2")
    print("5. cos(x ^ 3 + 2 * x ^ 2 + 7)")
    print("6. e ^ cos(x) - 1")
    print("7. cos(e ^ (x / 5))")
    print("8. (e ^ x) ^ 2 - sin(x) - cos(x)")
    print("9. e ^ (x ^ 2) - 5")
    print("10. Powrót to menu głównego")
    print("=======================================================================")


def chose_condition():
    print("\n===== Wybór warunku stopu algorytmu =====")
    print("1. Osiągnięcie zadanej dokładności")
    print("2. Osiągnięcie zadanej liczby iteracji")
    print("=========================================")
    cond = int(input("Twój wybór: "))
    return cond
