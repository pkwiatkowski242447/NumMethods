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


def calculate(function_number, start, end):                                         # function_num oznacza numer wybranej przez użytkownika funkcji
    print("Funkcja przeznaczona do obliczania miejsc zerowych zadanej funkcji.")    # start to początek przedziału, na którym szukane będzie miejsce zerowe
                                                                                    # end oznacza koniec tego przedziału


def main():
    user_choice = 0
    while user_choice != 2:
        print_menu()
        user_choice = int(input("Twój wybór: "))
        if user_choice != 2:
            clear()
            chose_functions()
            function_choice = int(input("Twój wybór: "))
            if function_choice > 10 or function_choice < 1:
                print("Wybrano nieprawidłową opcję z menu.")
                input("Wciśnij klawisz aby kontynuować...")
                clear()
            elif function_choice != 10:
                start = input("Podaj początek przedziału, na którym szukane będzie miejsce zerowe: ")
                end = input("Podaj koniec przedziału, na którym szukane będzie miejsce zerowe: ")
                clear()
                show_graph(function_choice)
                calculate(function_choice, start, end)
            else:
                clear()


if __name__ == '__main__':
    main()
