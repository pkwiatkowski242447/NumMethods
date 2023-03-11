import numpy
import math


def horner(x, tablica):
    wynik_h = tablica[0]
    for i in range(1, len(tablica), 1):
        wynik_h = wynik_h * x + tablica[i]
    return wynik_h


def y(x, funkcja):
    wynik = 0.0
    wspolczynniki = [1, 2, 0, 7]
    if funkcja == 1:
        wynik = horner(x, wspolczynniki)
    elif funkcja == 2:
        wynik = numpy.cos(x)
    elif funkcja == 3:
        wynik = math.e ** x
    elif funkcja == 4:
        wynik = horner(numpy.cos(x), wspolczynniki)
    elif funkcja == 5:
        wynik = numpy.cos(horner(x), wspolczynniki)
    elif funkcja == 6:
        wynik = math.e ** numpy.cos(x)
    elif funkcja == 7:
        wynik = numpy.cos(math.e ** x)
    elif funkcja == 8:
        wynik = horner(math.e ** x, wspolczynniki)
    return wynik
