import math

import numpy as np


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


def horner_scheme(x, coefficients):
    result = coefficients[0]
    for i in range(1, len(coefficients), 1):
        result = result * x + coefficients[i]
    return result


def divided_diff(x_tab, y_tab):
    n = np.size(x_tab)
    F = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        F[i][0] = y_tab[i]
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x_tab[i + j] - x_tab[i])
    return F


def newton_interpolation(x, x_tab, y_tab):
    F = divided_diff(x_tab, y_tab)
    n = np.size(x_tab) - 1
    p = F[n]
    for k in range(1, n + 1):
        p = F[n - k] + (x - x_tab[n - k]) * p
    return p


def y_values(int_nodes, function_choice):
    result = []
    for i in int_nodes:
        result.append(function_value(i, function_choice))
    return result
