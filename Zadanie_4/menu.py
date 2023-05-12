from numpy import double
import functions


def menu_start():
    while True:
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
        print("11. Koniec działania programu")
        function_choice = int(input("Wybierz funkcję: "))
        if 0 < function_choice < 11:
            eps = double(input("Podaj dokładność: "))
            print("1.Złożona kwadratura Newtona-Cotesa oparta na trzech węzłach")
            print("2.Kwadratura Gaussa na przedziale [-1,1] z wagą 1/sqrt(1-x^2)")
            method_choice = int(input("Wybierz metodę: "))
            if method_choice == 1:
                print(functions.calculate_integral_newton_cotes(function_choice, eps))
            if method_choice == 2:
                nodes = int(input("Ile chcesz węzłów: "))
                print(functions.calculate_integral_gauss(nodes, function_choice))
        elif function_choice == 11:
            break
        else:
            print("Mierny wybór")
