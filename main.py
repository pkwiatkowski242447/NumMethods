import math
import matplotlib.pyplot as plt
import numpy as np
import menu as mn
import calc as cl
import addon as ad


def show_graph(function_num, start, end):   # function_num oznacza numer wybranej przez użytkownika funkcji
    if start > end:
        print("Nieprawidłowa kolejność krańcy przedziału.")
    else:
        x = np.linspace(start, end, (ad.round_value(end) - ad.round_value(start)) * 20)
        match function_num:
            case 1:
                y = cl.horner_scheme(x, [1, 2, 0, 7], 4)
                func = "x ^ 3 + 2 * x ^ 2 + 7"
            case 2:
                func = "tg(x)"
                y = []
                for i in range(x.size):
                    y.append(math.tan(x[i]))
            case 3:
                func = "e ^ x"
                y = math.e ** x
            case 4:
                func = "(tg(x)) ^ 3 + 2 * (tg(x)) ^ 2 + 7"
                y = []
                for i in range(x.size):
                    y.append(cl.horner_scheme(math.tan(x[i]), [1, 2, 0, 7], 4))
            case 5:
                func = "tg(x ^ 3 + 2 * x ^ 2 + 7)"
                y = []
                for i in range(x.size):
                    y.append(math.tan(cl.horner_scheme(x[i], [1, 2, 0, 7], 4)))
            case 6:
                func = "e ^ tg(x)"
                y = []
                for i in range(x.size):
                    y.append(math.e ** math.tan(x[i]))
            case 7:
                func = "tg(e ^ x)"
                y = []
                for i in range(x.size):
                    y.append(math.tan(math.e ** x[i]))
            case 8:
                func = "(e ^ x) ^ 3 + 2 * (e ^ x) ^ 2 + 7"
                y = []
                for i in range(x.size):
                    y.append(cl.horner_scheme(math.e ** x[i], [1, 2, 0, 7], 4))
            case 9:
                func = "e ^ (x ^ 3 + 2 * x ^ 2 + 7)"
                y = []
                for i in range(x.size):
                    y.append(math.e ** (cl.horner_scheme(x[i], [1, 2, 0, 7], 4)))
            case _:
                print("Wybrano opcję spoza menu")
        plt.subplots(1, 1, figsize=(10, 14))
        plt.plot(x, y)
        plt.xlim((start - 0.25, end + 0.25))
        plt.ylim((-10.0, 20.0))
        plt.xticks(np.arange(start, end + 0.1, step=1))
        plt.yticks(np.arange(-10.0, 20.1, step=2.5))
        plt.xlabel("Oś OX")
        plt.ylabel("Oś OY")
        plt.title("Wykres funkcji o wzorze y = " + func)
        plt.grid()
        plt.show()
        input("Naciśnij klawisz, aby kontynuować...")
        ad.clear()


def main():
    user_choice = 0
    while user_choice != 2:
        ad.clear()
        mn.print_menu()
        user_choice = int(input("Twój wybór: "))
        if user_choice == 1:
            ad.clear()
            mn.chose_functions()
            function_choice = int(input("Twój wybór: "))
            if function_choice > 10 or function_choice < 1:
                print("Wybrano nieprawidłową opcję z menu.")
                input("Wciśnij klawisz aby kontynuować...")
                ad.clear()
            elif function_choice != 10:
                show_graph(function_choice, -5, 5)
                start = float(input("\nPodaj początek przedziału, na którym szukane będzie miejsce zerowe: "))
                end = float(input("Podaj koniec przedziału, na którym szukane będzie miejsce zerowe: "))
                stop_cond = 0
                val = 0
                while stop_cond != 1 and stop_cond != 2:
                    stop_cond = mn.chose_condition()
                    if stop_cond == 1:
                        val = float(input("Podaj oczekiwaną dokładność: "))
                    elif stop_cond == 2:
                        val = int(input("Podaj oczekiwaną liczbę interacji: "))
                    else:
                        print("Podano nieprawidłową opcję z menu")
                        ad.clear()
                ad.clear()
                cl.calculate(function_choice, start, end, stop_cond, val)
                show_graph(function_choice, start, end)
            else:
                ad.clear()
        elif user_choice != 1 and user_choice != 2:
            print("Podano nieprawidłową opcję.")
            input("Naciśnij dowolny klawisz aby kontynuować...")
            ad.clear()


if __name__ == '__main__':
    main()
