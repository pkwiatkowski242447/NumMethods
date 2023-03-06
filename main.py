def menu_start():
    while True:
        print("1.Wielomian")
        print("2.Trygonometryczna")
        print("3.Wykładnicza")
        print("4.Koniec")
        wybor_funkcji = int(input("Wybierz: "))
        if wybor_funkcji == 1 or wybor_funkcji == 2 or wybor_funkcji == 3:
            podstawowy_wybor()
        elif wybor_funkcji == 4:
            break
        else:
            print("Mierny wybór")


def podstawowy_wybor():
    wybor_przedzialu_LEWO = int(input("Podaj lewy krawniec przedziału na którym poszukiwane będzie miejsce zerowe: "))
    wybor_przedzialu_PRAWO = int(input("Podaj prawy kraniec przedziału na którym poszukiwane będzie miejsce zerowe: "))
    print("a.Spełnienie warunku nałożonego na dokładność")
    print("b.Osiągnięcie zadanej liczby iteracji")
    wybor_zatrzymania = input("Podaj kryterium zatrzymania algorytmu: ")
    if wybor_zatrzymania == "a":
        wybor_epsilon = input("Wprowadź ε: ")
        wybor_epsilon.strip()
    elif wybor_zatrzymania == "b":
        wybor_iteracji = input("Podaj liczbe iteracji: ")
        wybor_iteracji.strip()
    else:
        print("Blad wyboru")


if __name__ == '__main__':
    menu_start()
