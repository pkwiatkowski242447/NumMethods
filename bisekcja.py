import numpy


def horner(x, tablica):
    wynik_h = tablica[0]
    for i in range(1, len(tablica), 1):
        wynik_h = wynik_h * x + tablica[i]
    return wynik_h


def y(x, funkcja):
    wynik = 0.0
    if funkcja == 1:
        wspolczynniki = [2, 3, 4, -1]
        wynik = horner(x, wspolczynniki)
    elif funkcja == 2:
        wynik = numpy.tan(x)
    elif funkcja == 3:
        wynik = 0.5 ** x
    return wynik


def bisekcja_epsilon(x1, x2, eps, f):
    x = 0
    liczba_iteracji = 0
    f_a = y(x1, f)
    f_b = y(x2, f)
    if f_a * f_b > 0:
        print("Funkcja nie ma różnych znaków na krańcach przedziału")
    else:
        while abs(x2 - x1) > eps:
            liczba_iteracji += 1
            x = (x1 + x2) / 2
            f_srodek = y(x, f)
            if f_b * f_srodek < 0:
                x1 = x
            else:
                x2 = x
                f_b = f_srodek
        return [x, liczba_iteracji]


def bisekcja_iteracyjna(x1, x2, i, f):
    x = 0
    f_a = y(x1, f)
    f_b = y(x2, f)
    if f_a * f_b > 0:
        print("Funkcja nie ma różnych znaków na krańcach przedziału")
    else:
        while i > 0:
            i -= 1
            x = (x1 + x2) / 2
            f_srodek = y(x, f)
            if f_b * f_srodek < 0:
                x1 = x
            else:
                x2 = x
                f_b = f_srodek
        return x
