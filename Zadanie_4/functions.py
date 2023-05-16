import math

import numpy as np


def y(x, function):
    if function == 1:
        return 0.2 * x - 1.2
    if function == 2:
        return 0.7 * abs(x) - 2.0
    if function == 3:
        return math.sin(x)
    if function == 4:
        return math.pow(x, 3) - 3 * math.pow(x, 2) - 1
    if function == 5:
        return math.pow(math.sin(x), 3) - 2 * abs(math.cos(x))
    if function == 6:
        return math.pow(2, x)
    if function == 7:
        return math.sin(7 * x + 6)
    if function == 8:
        return math.pow(math.sin(2 * x), 3) - 1
    if function == 9:
        return math.pow(abs(x), 3) - 2 * abs(x) + 8
    if function == 10:
        return 8.1 * math.sin(x) + x


def calculate_integral_newton_cotes(function, a, b, epsilon):
    number_of_intervals = 1
    previous_integral_value = 0.0
    integral_value = calculate_integral_simpson(function, a, b, number_of_intervals)

    while abs(integral_value - previous_integral_value) >= epsilon:
        previous_integral_value = integral_value
        number_of_intervals *= 2
        integral_value = calculate_integral_simpson(function, a, b, number_of_intervals)

    return integral_value


def calculate_integral_simpson(function, a, b, number_of_intervals):
    interval_length = (b - a) / number_of_intervals
    integral_value = 0.0

    for i in range(number_of_intervals):
        x0 = a + i * interval_length
        x1 = a + (i + 0.5) * interval_length
        x2 = a + (i + 1) * interval_length

        integral_value += (interval_length / 6) * (
                y(x0, function) + 4 * y(x1, function) + y(x2, function))

    return integral_value


def calculate_integral_gauss(n, function):
    nodes = np.cos((2 * np.arange(n) + 1) * np.pi / (2 * n))  # Miejsca zerowe Czebyszewa
    weights = np.pi / n  # Wagi

    result = 0.0
    for i in range(n):
        result += weights * y(nodes[i], function)

    return result
