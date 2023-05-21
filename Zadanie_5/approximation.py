import numpy as np

from functions import function_value
from quadrature import calculate_definite_integral_gauss
from polynomials import evaluate_polynomial


def calculate_approximation(function_choice, approximation_interval, polynomial_degree, number_of_nodes):
    a, b = approximation_interval
    coefficients = []
    for k in range(polynomial_degree + 1):
        integral_value = calculate_definite_integral_gauss(function_choice, number_of_nodes)
        coefficient = (2 / (b - a)) * integral_value
        coefficients.append(coefficient)
        number_of_nodes += 1

    approximation_error = calculate_approximation_error(
        function_choice, approximation_interval, coefficients
    )

    return coefficients, np.max(approximation_error), np.mean(approximation_error)


def calculate_approximation_error(function_choice, approximation_interval, coefficients):
    a, b = approximation_interval
    x_vals = np.linspace(a, b, 1000)
    y_vals_original = [function_value(function_choice, x) for x in x_vals]
    y_vals_approximation = [evaluate_polynomial(coefficients, x) for x in x_vals]
    approximation_error = np.abs(np.array(y_vals_original) - np.array(y_vals_approximation))
    return approximation_error
