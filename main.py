import os
import matplotlib.pyplot as plt
import numpy as np


def print_menu():
    print("===== Menu =====")
    print("1. Wybór funkcji do wyznaczenia miejsc zerowych i wyświetlenia.")
    print("2. Zakończenie działania programu")
    print("================")


def clear():
    if os.name == 'posix':
        os.system('clear')      # Czyszczenie konsoli dla systemów Linux / Mac
    else:
        os.system('cls')        # Czyszczenie konsoli dla systemu Windows


def chose_functions():
    print("===== Wybór funkcji od wyświetlenia i wyznaczenia miejsc zerowych =====")
    print("1. x^3 + 2x^2 + 7")
    print("2. ctg(x)")
    print("3. e^x")
    print("4. (ctg(x))^3 + 2(ctg(x))^2 + 7")
    print("5. ctg(x^3 + 2x^2 + 7)")
    print("6. e ^ ctg(x)")
    print("7. ctg(e ^ x)")
    print("8. (e ^ x) ^ 3 + 2(e ^ x) ^ 2 + 7")
    print("9. e ^ (x^3 + 2x^2 + 7)")
    print("10. Powrót to menu głównego")
    print("=======================================================================")


def show_graph(function_num):   # function_num oznacza numer wybranej przez użytkownika funkcji
    print("Funkcja do wyświetlania wykresu zadanej funkcji.")
    input("Naciśnij klawisz, aby kontynuować...")
    clear()


def calculate(function_number, start, end, cond, value):                            # function_num oznacza numer wybranej przez użytkownika funkcji
    print("Funkcja przeznaczona do obliczania miejsc zerowych zadanej funkcji.")    # start to początek przedziału, na którym szukane będzie miejsce zerowe
    input("Naciśnij klawisz, aby kontynuować...")                                   # end oznacza koniec tego przedziału
    clear()                                                                         # cond oznacza wybrany przez użytkownika warunek stopu
                                                                                    # value to wartość dotycząca warunku stopu, a więc liczba iteracji lub też zadana dokładność


def chose_condition():
    print("\n===== Wybór warunku stopu algorytmu =====")
    print("1. Osiągnięcie zadanej dokładności")
    print("2. Osiągnięcie zadanej liczby iteracji")
    print("=========================================")
    cond = int(input("Twój wybór: "))
    return cond


def main():
    user_choice = 0
    while user_choice != 2:
        clear()
        print_menu()
        user_choice = int(input("Twój wybór: "))
        if user_choice == 1:
            clear()
            chose_functions()
            function_choice = int(input("Twój wybór: "))
            if function_choice > 10 or function_choice < 1:
                print("Wybrano nieprawidłową opcję z menu.")
                input("Wciśnij klawisz aby kontynuować...")
                clear()
            elif function_choice != 10:
                start = input("\nPodaj początek przedziału, na którym szukane będzie miejsce zerowe: ")
                end = input("Podaj koniec przedziału, na którym szukane będzie miejsce zerowe: ")
                stop_cond = 0
                val = 0
                while stop_cond != 1 and stop_cond != 2:
                    stop_cond = chose_condition()
                    if stop_cond == 1:
                        val = float(input("Podaj oczekiwaną dokładność: "))
                    elif stop_cond == 2:
                        val = int(input("Podaj oczekiwaną liczbę interacji: "))
                    else:
                        print("Podano nieprawidłową opcję z menu")
                        clear()
                clear()
                show_graph(function_choice)
                calculate(function_choice, start, end, stop_cond, val)
            else:
                clear()
        elif user_choice != 1 and user_choice != 2:
            print("Podano nieprawidłową opcję.")
            input("Naciśnij dowolny klawisz aby kontynuować...")
            clear()


if __name__ == '__main__':
    main()
