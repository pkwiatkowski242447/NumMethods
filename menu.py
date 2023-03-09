from numpy import double
import bisekcja as b


def menu_start():
    while True:
        print("1.Wielomian np.2x^3+3x^2+4x-1")
        print("2.Trygonometryczna np.tg(x)")
        print("3.Wykładnicza np. (1/2)^x")
        print("4.Koniec działania programu")
        wybor_funkcji = int(input("Wybierz: "))
        if wybor_funkcji == 1 or wybor_funkcji == 2 or wybor_funkcji == 3:
            podstawowy_wybor()
        elif wybor_funkcji == 4:
            break
        else:
            print("Mierny wybór")


def podstawowy_wybor():
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
            print("Wynik: " + str(b.bisekcja_epsilon(x1, x2, wybor_epsilon, 1)[0]))
            print("Liczba iteracji: " + str(b.bisekcja_epsilon(x1,x2,wybor_epsilon,1)[1]))
        elif wybor_zatrzymania == "b":
            wybor_iteracji = int(input("Podaj liczbe iteracji: "))
            print("Wynik: " + str(b.bisekcja_iteracyjna(x1, x2, wybor_iteracji, 1)))
        else:
            print("Blad wyboru")
