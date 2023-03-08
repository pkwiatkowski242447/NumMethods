import numpy


def horner(x, tablica):
    wynik_h = tablica[0]
    for i in range(1, len(tablica), 1):
        wynik_h = wynik_h * x + tablica[i]
    return wynik_h


def obliczanie_wartosci_funkcji(x, funkcja):
    wynik = 0.0
    if funkcja == 1:
        wspolczynniki = [2, 3, 4, -1]
        wynik = horner(x, wspolczynniki)
    elif funkcja == 2:
        wynik = numpy.tan(x)
    elif funkcja == 3:
        wynik = 0.5 ** x
    return wynik


def bisekcja(poczatek, koniec, epsilon, funkcja):
    liczba_iteracji = 0
    f_a = obliczanie_wartosci_funkcji(poczatek, funkcja)
    f_b = obliczanie_wartosci_funkcji(koniec, funkcja)
    if f_a * f_b > 0:
        print("Funkcja nie ma różnych znaków na krańcach przedziału")
    else:
        while abs(koniec - poczatek) > epsilon:
            liczba_iteracji += 1
            srodek = (poczatek + koniec) / 2
            f_srodek = obliczanie_wartosci_funkcji(srodek, funkcja)
            if f_b * f_srodek < 0:
                poczatek = srodek
            else:
                koniec = srodek
                f_b = f_srodek
        return srodek, liczba_iteracji
