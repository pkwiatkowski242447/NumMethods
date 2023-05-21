from approximation import calculate_approximation
from functions import function_value
from polynomials import evaluate_polynomial
import numpy as np
import matplotlib.pyplot as plt


def run_program():
    function_choices = ["linear", "absolute", "polynomial", "trigonometric", "composite"]

    print("Available functions:")
    for i, function_choice in enumerate(function_choices, start=1):
        print(f"{i}. {function_choice}")

    function_choice = int(input("Choose a function (enter the corresponding number): "))
    function_choice = function_choices[function_choice - 1]

    approximation_interval = tuple()

    a = float(input("Enter the lower bound of the approximation interval (a): "))
    approximation_interval += (a,)

    b = float(input("Enter the upper bound of the approximation interval (b): "))
    approximation_interval += (b,)

    polynomial_degree = int(input("Enter the degree of the approximating polynomial: "))

    number_of_nodes = int(input("Enter the number of nodes for Gauss quadrature: "))

    coefficients, max_error, mean_error = calculate_approximation(
        function_choice, approximation_interval, polynomial_degree, number_of_nodes
    )

    print(f"\nCoefficients of the approximating polynomial: {coefficients}")
    print(f"Maximum approximation error: {max_error}")
    print(f"Mean approximation error: {mean_error}")

    x_vals = np.linspace(approximation_interval[0], approximation_interval[1], 1000)
    y_vals_original = [function_value(function_choice, x) for x in x_vals]
    y_vals_approximation = [evaluate_polynomial(coefficients, x) for x in x_vals]

    plt.plot(x_vals, y_vals_original, label="Original Function")
    plt.plot(x_vals, y_vals_approximation, label="Approximation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Approximation using Chebyshev Polynomials")
    plt.show()


run_program()
