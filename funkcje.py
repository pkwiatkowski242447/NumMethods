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
