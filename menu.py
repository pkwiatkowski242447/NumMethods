from numpy import double
import bisection as b
import secant as s
import graphs as w


def menu_start():
    while True:
        print("1. x ^ 3 + 2 * x ^ 2 + 7")
        print("2. cos(x)")
        print("3. e ^ x")
        print("4. (cos(x)) ^ 3 + 2 * (cos(x)) ^ 2 + 7")
        print("5. cos(x ^ 3 + 2 * x ^ 2 + 7)")
        print("6. e ^ cos(x)")
        print("7. cos(e ^ x)")
        print("8. (e ^ x) ^ 3 + 2 * (e ^ x) ^ 2 + 7")
        print("9. Koniec działania programu")
        function_choice = int(input("Wybierz funkcję: "))
        if 0 < function_choice < 9:
            podstawowy_wybor(function_choice)
        elif function_choice == 9:
            break
        else:
            print("Mierny wybór")


def podstawowy_wybor(function_choice):
    x1 = double(
        input("Podaj lewy kraniec przedziału na którym poszukiwane będzie miejsce zerowe: "))
    x2 = double(
        input("Podaj prawy kraniec przedziału na którym poszukiwane będzie miejsce zerowe: "))
    if x1 >= x2:
        print("Lewy kraniec przedziału musi być mniejszy niż prawy koniec przedziału")
    else:
        w.inital_graph(function_choice, x1, x2)
        print("a.Spełnienie warunku nałożonego na dokładność")
        print("b.Osiągnięcie zadanej liczby iteracji")
        wybor_zatrzymania = input("Podaj kryterium zatrzymania algorytmu: ")
        if wybor_zatrzymania == "a":
            wybor_epsilon = double(input("Wprowadź ε: "))
            x_value_bisection = b.bisection(x1, x2, function_choice, "a", wybor_epsilon)[0]
            i_value_bisection = b.bisection(x1, x2, function_choice, "a", wybor_epsilon)[1]
            x_value_secant = s.secant(x1, x2, function_choice, "a", wybor_epsilon)[0]
            i_value_secant = s.secant(x1, x2, function_choice, "a", wybor_epsilon)[1]
            print("Wynik osiągnięty metodą bisekcji: " + str(x_value_bisection))
            print("Po: " + str(i_value_bisection) + " liczbie iteracji")
            print("Wynik osiągnięty metodą siecznych: " + str(x_value_secant))
            print("Po: " + str(i_value_secant) + " liczbie iteracji")
            w.final_graph(function_choice, x1, x2,
                          x_value_bisection,
                          x_value_secant)
        elif wybor_zatrzymania == "b":
            wybor_iteracji = int(input("Podaj liczbe iteracji: "))
            print("Wynik osiągnięty metodą bisekcji: " + str(b.bisection(x1, x2, function_choice, "b", wybor_iteracji)))
            print("Wynik osiągnięty metodą siecznych: " + str(s.secant(x1, x2, function_choice, "b", wybor_iteracji)))
            w.final_graph(function_choice, x1, x2,
                          b.bisection(x1, x2, function_choice, "b", wybor_iteracji),
                          s.secant(x1, x2, function_choice, "b", wybor_iteracji))
        else:
            print("Blad wyboru")
