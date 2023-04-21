import math

import numpy as np

"""
function_value oblicza wartość funkcji w punkcie, przyjmuje następujące argumenty:
    x -> wartośc argumentu 
    function_choice -> funkcja wbudowana w programie wcześniej wybrana przez użytkownika 
    1. Funkcja liniowa
    2. Funkcja liniowa z wartością bezwzględną argumentu funkcji 
    3. Funkcja sinus 
    4. Funkcja wielomianowa
    5. Funkcja cosinus
    6. Funkcja złożona 
    7. Funkcja wielomianowa z zagnieżdżoną funkcją trygonometryczną
    8. Funkcja cosinus z zagnieżdżoną wartością bezwzględną 
    9. Funkcja wartości bezwzględnej z funkcją sinus i cosinus 
    10. Funkcja wielomianowa z wartością bezwzględną 
"""


def function_value(x, function_choice):
    coeff_function_4 = [1, 1, 4]
    coeff_function_7 = [1, 0, 0, -1]
    coeff_function_10 = [1, -2, 8]
    match function_choice:
        case 1:
            y_value = 2.3 * x + 0.5
        case 2:
            y_value = 2 * abs(x) - 2.5
        case 3:
            y_value = math.sin(x)
        case 4:
            y_value = horner_scheme(x, coeff_function_4)
        case 5:
            y_value = math.cos(7 * x + 6)
        case 6:
            y_value = 8.1 * math.sin(x) + x
        case 7:
            y_value = horner_scheme(math.sin(2 * x), coeff_function_7)
        case 8:
            y_value = math.cos(abs(x)) - 2
        case 9:
            y_value = abs(math.sin(x)) + abs(math.cos(x))
        case 10:
            y_value = horner_scheme(abs(x), coeff_function_10)
        case _:
            y_value = 0
    return y_value


"""
horner_scheme -> funkcja implementująca algorytm Hornera. 
    x -> punkt
    coefficients -> współczynniki wielomianu 
"""


def horner_scheme(x, coefficients):
    result = coefficients[0]
    for i in range(1, len(coefficients), 1):
        result = result * x + coefficients[i]
    return result


"""
newton_interpolation -> funkcja implementująca interpolację Newtona dla nierównych odstępów argumentów
    x -> punkt 
    x_tab -> tablica węzłów intepolacyjnych 
    y_tab -> wartości funkcji dla węzłów interpolacji 
    1.Obliczanie ile jest węzłów interpolacyjnych
    2.Wypełnienie tablicy F o wymiarach n x n zerami 
    3.Następnie wypełnienie wiersza 0 wartościami z tablicy y_tab
    4.Wypełnienie kolejnych kolumn tablicy obliczonymi różnicami dzielonych
    5.Obliczenie wartości interpolowanego wielomianu w punkcie x przy użyciu interpolacyjnej formuły Newtona
    6.Zwrócenie wartości interpolowanego wielomianu w punkcie x przy użyciu interpolacyjnej formuły Newtona
"""


def newton_interpolation(x, x_tab, y_tab):
    n = len(x_tab)
    F = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        F[i][0] = y_tab[i]
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x_tab[i + j] - x_tab[i])
    result = F[0][n - 1]
    for i in range(n - 2, -1, -1):
        result = F[0][i] + (x - x_tab[i]) * result
    return result


def y_values_interp_nodes(int_nodes, function_choice):
    result = []
    for i in int_nodes:
        result.append(function_value(i, function_choice))
    return result
