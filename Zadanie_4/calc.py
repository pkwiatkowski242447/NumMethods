import math


def function_value(function_choice, arg):
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
        case "6":
            return math.pow(2, arg)
        case "7":
            return math.sin(7 * arg + 6)
        case "8":
            return math.pow(math.sin(2 * arg), 3) - 1
        case "9":
            return math.pow(abs(arg), 3) - 2 * abs(arg) + 8
        case "10":
            return 8.1 * math.sin(arg) + arg
        case other:
            return None


def get_weight_function_value(arg_value):
    return 1 / math.sqrt(1 - math.pow(arg_value, 2))


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


def calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side):
    number_of_intervals = 1
    previous_integral_value = calculate_integral_simpson_method(function_choice, number_of_intervals, left_side, right_side)
    number_of_intervals *= 2
    integral_value = calculate_integral_simpson_method(function_choice, number_of_intervals, left_side, right_side)
    while abs(integral_value - previous_integral_value) >= epsilon:
        previous_integral_value = integral_value
        number_of_intervals *= 2
        integral_value = calculate_integral_simpson_method(function_choice, number_of_intervals, left_side, right_side)
    return integral_value


def calculate_integral_simpson_method(function_choice, number_of_intervals, left_side, right_side):
    interval_length = abs(right_side - left_side)
    sub_interval_length = interval_length / number_of_intervals
    integral_value = 0
    for i in range(0, number_of_intervals):
        a = left_side + i * sub_interval_length
        b = a + sub_interval_length
        integral_value += ((b - a) / 6) * (function_value(function_choice, a) * get_weight_function_value(a)
            + 4 * function_value(function_choice, (a + b) / 2) * get_weight_function_value((a + b) / 2)
            + function_value(function_choice, b) * get_weight_function_value(b))
    return integral_value


def get_limit_value_for_newton_cotes(function_choice, epsilon):
    left_side = 0
    right_side = 0.5
    integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side)
    actual_integral_value = integral_iteration_value
    iteration_number = 0
    while abs(integral_iteration_value) >= epsilon:
        iteration_number += 1
        left_side = right_side
        right_side += 0.5 * math.pow(0.5, iteration_number)
        integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side)
        actual_integral_value += integral_iteration_value
    right_side = 0
    left_side = -0.5
    integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side)
    actual_integral_value += integral_iteration_value
    iteration_number = 0
    while abs(integral_iteration_value) >= epsilon:
        iteration_number += 1
        right_side = left_side
        left_side += -0.5 * math.pow(0.5, iteration_number)
        integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side)
        actual_integral_value += integral_iteration_value
    return actual_integral_value
