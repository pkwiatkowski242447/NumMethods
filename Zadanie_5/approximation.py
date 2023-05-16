import numpy as np
import matplotlib.pyplot as plt
from functions import *
from integration_methods import *


def chebyshev_approximation(f, interval, degree, integration_method, num_nodes):
    a, b = interval
    nodes, weights = integration_method(num_nodes, a, b)
    x = 0.5 * (a + b) + 0.5 * (b - a) * np.cos(np.pi * nodes)
    f_values = f(x)

    coefficients = []
    for k in range(degree + 1):
        c = 0.0
        for j in range(num_nodes):
            c += weights[j] * f_values[j] * np.cos(k * np.arccos(nodes[j]))
        c *= 2.0 / num_nodes
        coefficients.append(c)

    return coefficients


def horner_evaluation(coefficients, x):
    result = coefficients[-1]
    for i in range(len(coefficients) - 2, -1, -1):
        result = result * x + coefficients[i]
    return result


def plot_function(f, interval):
    x = np.linspace(interval[0], interval[1], 1000)
    y = f(x)

    plt.plot(x, y, label='Original Function')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def plot_approximation(f, interval, degree, coefficients):
    x = np.linspace(interval[0], interval[1], 1000)
    y_original = f(x)
    y_approximation = np.array([horner_evaluation(coefficients, xi) for xi in x])

    plt.plot(x, y_original, label='Original Function')
    plt.plot(x, y_approximation, label='Approximation (Degree: {})'.format(degree))
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def calculate_approximation_error(f, interval, degree, coefficients, num_points=1000):
    x = np.linspace(interval[0], interval[1], num_points)
    y_original = f(x)
    y_approximation = np.array([horner_evaluation(coefficients, xi) for xi in x])
    error = np.linalg.norm(y_original - y_approximation)
    return error
