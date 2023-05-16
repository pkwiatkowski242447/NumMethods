from functions import *
from approximation import *


def print_function_options():
    print("Choose a function to approximate:")
    print("1. Linear")
    print("2. Absolute Value")
    print("3. Polynomial")
    print("4. Trigonometric")
    print("5. Composite")


def print_integration_options():
    print("Choose an integration method:")
    print("1. Gauss-Legendre Quadrature")
    print("2. Gauss-Chebyshev Quadrature")


def get_user_choice(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        print("Invalid choice. Please try again.")


def perform_approximation():
    function_mapping = {
        '1': linear,
        '2': absolute,
        '3': polynomial,
        '4': trigonometric,
        '5': composite
    }

    print_function_options()
    function_choice = get_user_choice("Enter the corresponding number: ", function_mapping)

    f = function_mapping[function_choice]

    interval = tuple(map(float, input('Enter the interval (e.g., -1 1): ').split()))

    degree = int(input('Enter the degree of the approximation polynomial: '))

    print_integration_options()
    integration_choice = get_user_choice("Enter the corresponding number: ", ["1", "2"])

    if integration_choice == '1':
        integration_method = gauss_legendre
    else:
        integration_method = gauss_chebyshev

    num_nodes = int(input('Enter the number of integration nodes: '))

    coefficients = chebyshev_approximation(f, interval, degree, integration_method, num_nodes)

    plot_function(f, interval)
    plot_approximation(f, interval, degree, coefficients)

    error = calculate_approximation_error(f, interval, degree, coefficients)
    print('Approximation error:', error)


perform_approximation()
