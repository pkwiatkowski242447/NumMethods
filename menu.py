from numpy import double
import bisekcja as b
import sieczne as s
import wykresy as w

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
        wybor_funkcji = int(input("Wybierz funkcję: "))
        if 0 < wybor_funkcji < 9:
            podstawowy_wybor(wybor_funkcji)
        elif wybor_funkcji == 9:
            break
        else:
            print("Mierny wybór")


def podstawowy_wybor(wybor_f):
    x1 = double(
        input("Podaj lewy kraniec przedziału na którym poszukiwane będzie miejsce zerowe: "))
    x2 = double(
        input("Podaj prawy kraniec przedziału na którym poszukiwane będzie miejsce zerowe: "))
    if x1 >= x2:
        print("Lewy kraniec przedziału musi być mniejszy niż prawy koniec przedziału")
    else:
        print("a.Spełnienie warunku nałożonego na dokładność")
        print("b.Osiągnięcie zadanej liczby iteracji")
        wybor_zatrzymania = input("Podaj kryterium zatrzymania algorytmu: ")
        if wybor_zatrzymania == "a":
            wybor_epsilon = double(input("Wprowadź ε: "))
            b.bisekcja(x1, x2, wybor_f, "a", wybor_epsilon)
            s.sieczne(x1, x2, wybor_f, "a", wybor_epsilon)
            w.wykres(wybor_f,x1,x2)
        elif wybor_zatrzymania == "b":
            wybor_iteracji = int(input("Podaj liczbe iteracji: "))
            b.bisekcja(x1, x2, wybor_f, "b", wybor_iteracji)
            s.sieczne(x1, x2, wybor_f, "b", wybor_iteracji)
        else:
            print("Blad wyboru")
