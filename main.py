import matplotlib.pyplot as plt
import numpy as np
import menu as mn
import calc as cl
import addon as ad


def show_graph(function_num, start, end):   # function_num oznacza numer wybranej przez użytkownika funkcji
    if start > end:
        print("Nieprawidłowa kolejność krańcy przedziału.")
    else:
        x = np.linspace(start, end, (ad.round_value(end) - ad.round_value(start)) * 200)
        y = []
        if 0 < function_num <= 9:
            for i in range(x.size):
                y.append(cl.function_value(x[i], function_num))
        else:
            print("Podano nieprawidłową opcję z menu")
        plt.subplots(1, 1, figsize=(10, 14))
        plt.plot(x, y)
        plt.xlim((start - 0.25, end + 0.25))
        plt.ylim((-10.0, 20.0))
        plt.xticks(np.arange(start, end + 0.1, step=1))
        plt.yticks(np.arange(-10.0, 20.1, step=2.5))
        plt.xlabel("Oś OX")
        plt.ylabel("Oś OY")
        plt.title("Wykres wybranej funkcji")
        plt.grid()
        plt.show()
        input("\nNaciśnij klawisz, aby kontynuować...")
        ad.clear()


def show_graph_with_points(function_num, start, end, zero_b, zero_s):
    if start > end:
        print("Nieprawidłowa kolejność krańcy przedziału.")
    else:
        x = np.linspace(start, end, (ad.round_value(end) - ad.round_value(start)) * 200)
        y = []
        if 0 < function_num <= 9:
            for i in range(x.size):
                y.append(cl.function_value(x[i], function_num))
        else:
            print("Podano nieprawidłową opcję z menu")
        plt.subplots(1, 1, figsize=(10, 14))
        plt.plot(x, y)
        plt.xlim((start - 0.25, end + 0.25))
        plt.ylim((-10.0, 20.0))
        plt.xticks(np.arange(start, end + 0.1, step=1))
        plt.yticks(np.arange(-10.0, 20.1, step=2.5))
        plt.xlabel("Oś OX")
        plt.ylabel("Oś OY")
        plt.title("Wykres wybranej funkcji")
        plt.grid()
        if zero_b is not None:
            plt.plot(zero_b, cl.function_value(zero_b, function_num), marker="o", markerfacecolor="orange")
        if zero_s is not None:
            plt.plot(zero_s, cl.function_value(zero_s, function_num), marker="o", markerfacecolor="purple")
        plt.show()
        input("\nNaciśnij klawisz, aby kontynuować...")
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
                start = float(input("Podaj początek przedziału, na którym szukane będzie miejsce zerowe: "))
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
                zero_b = cl.bisection(function_choice, start, end, stop_cond, val)
                zero_s = cl.secant_method(function_choice, start, end, stop_cond, val)
                if zero_b is not None or zero_s is not None:
                    show_graph_with_points(function_choice, start, end, zero_b, zero_s)
            else:
                ad.clear()
        elif user_choice != 1 and user_choice != 2:
            print("Podano nieprawidłową opcję.")
            input("Naciśnij dowolny klawisz aby kontynuować...")
            ad.clear()


if __name__ == '__main__':
    main()
