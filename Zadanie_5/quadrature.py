import math
from functions import function_value


def calculate_chebyshev_zeros(chebyshev_degree):
    list_of_zeros = []
    for i in range(chebyshev_degree):
        zero_value = math.cos(((2 * i + 1) / (2 * chebyshev_degree)) * math.pi)
        list_of_zeros.append(zero_value)
    return list_of_zeros


def calculate_definite_integral_gauss(function_choice, number_of_nodes):
    list_of_zeros = calculate_chebyshev_zeros(number_of_nodes + 1)
    coefficient_value = math.pi / (number_of_nodes + 1)
    integral_value = 0
    for i in list_of_zeros:
        integral_value += coefficient_value * function_value(function_choice, i)
    return integral_value
