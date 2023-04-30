import math


def function_value_for_newton_cotes(function_choice, arg):
    match function_choice:
        case "1":
            return (0.2 * arg - 1.2) / math.sqrt(1 - math.pow(arg, 2))
        case "2":
            return (0.7 * abs(arg) - 2.0) / math.sqrt(1 - math.pow(arg, 2))
        case "3":
            return math.sin(arg) / math.sqrt(1 - math.pow(arg, 2))
        case "4":
            return (math.pow(arg, 3) - 3 * math.pow(arg, 2) - 1) / math.sqrt(1 - math.pow(arg, 2))
        case "5":
            return math.pow(math.sin(arg), 3) - 2 * abs(math.cos(arg)) / math.sqrt(1 - math.pow(arg, 2))
        case other:
            return None


def function_value_for_gauss(function_choice, arg):
    match function_choice:
        case "1":
            return 0.2 * arg - 1.2
        case "2":
            return 0.7 * abs(arg) - 2.0
        case "3":
            return math.sin(arg)
        case "4":
            return math.pow(arg, 3) - 3 * math.pow(arg, 2) - 1
        case "5":
            return math.pow(math.sin(arg), 3) - 2 * abs(math.cos(arg))
        case other:
            return None


def calculate_czebyshev_zeros(number_of_nodes):


def calculate_quadrature_coefficients_values(number_of_nodes):
    if number_of_nodes