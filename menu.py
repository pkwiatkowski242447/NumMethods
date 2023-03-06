def print_menu():
    print("===== Menu =====")
    print("1. Wybór funkcji do wyznaczenia miejsc zerowych i wyświetlenia.")
    print("2. Zakończenie działania programu")
    print("================")


def chose_functions():
    print("===== Wybór funkcji od wyświetlenia i wyznaczenia miejsc zerowych =====")
    print("1. x ^ 3 + 2 * x ^ 2 + 7")
    print("2. tg(x)")
    print("3. e ^ x")
    print("4. (tg(x)) ^ 3 + 2 * (tg(x)) ^ 2 + 7")
    print("5. ctg(x ^ 3 + 2 * x ^ 2 + 7)")
    print("6. e ^ tg(x)")
    print("7. tg(e ^ x)")
    print("8. (e ^ x) ^ 3 + 2 * (e ^ x) ^ 2 + 7")
    print("9. e ^ (x ^ 3 + 2 * x ^ 2 + 7)") # W tym przpadku możliwe jest podanie -3 i -2.9 co spowoduje brak wykresu
    print("10. Powrót to menu głównego")
    print("=======================================================================")


def chose_condition():
    print("\n===== Wybór warunku stopu algorytmu =====")
    print("1. Osiągnięcie zadanej dokładności")
    print("2. Osiągnięcie zadanej liczby iteracji")
    print("=========================================")
    cond = int(input("Twój wybór: "))
    return cond
