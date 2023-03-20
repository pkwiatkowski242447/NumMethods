import numpy
import math


def horner(x, tab):
    result = tab[0]
    for i in range(1, len(tab), 1):
        result = result * x + tab[i]
    return result


def y(x, funkcja):
    result = 0.0
    coefficients = [1, 2, 0, 7]
    coefficients_2 = [1, 4, -21]
    if funkcja == 1:
        result = horner(x, coefficients)
    elif funkcja == 2:
        result = numpy.cos(x)
    elif funkcja == 3:
        result = math.e ** x
    elif funkcja == 4:
        result = horner(numpy.cos(x), coefficients)
    elif funkcja == 5:
        result = numpy.cos(horner(x), coefficients)
    elif funkcja == 6:
        result = math.e ** numpy.cos(x)
    elif funkcja == 7:
        result = numpy.cos(math.e ** x)
    elif funkcja == 8:
        result = horner(math.e ** x, coefficients)
    elif funkcja == 10:
        result = horner(x,coefficients_2)
    return result
