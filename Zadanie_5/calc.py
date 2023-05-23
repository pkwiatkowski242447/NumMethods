import math

import numpy as np
import matplotlib.pyplot as plt

"""
    @ Function: calculate_horner_scheme()
    
    @ Parameters: 
    
    * length_of_the_array   -> length of passed array of coefficients 
    * array_of_coefficients -> array containing coefficients (that is a0, a1, a2, ... an)
    * arg_value             -> argument for which function's value will be calculated
    
    @ Returns: Value of a polynomial of a length_of_the_array degree and coefficients inside array_of_coefficients
    in arg_value.
    
    @ Description: This method is used for calculating certain polynomial value in a arg_value. It takes as parameters
    length_of_the_array (which is degree of this polynomial) and array_of_coefficients (containing next coefficients).
    Based on that value of the polynomial is calculated.
"""


def calculate_horner_scheme(length_of_the_array, array_of_coefficients, arg_value):
    calculated_value = 0
    for index in range(length_of_the_array):
        calculated_value = calculated_value * arg_value + array_of_coefficients[index]
    return calculated_value


"""
    @ Function: calculate_function_value()
    
    @ Parameters:
    
    * function_choice   -> number of choosen function from the menu 
    * arg_value         -> argument value for which function (chosen by the user - that is function_choice) value
    will be calculated
    
    @ Retruns: Value of a function_choice function in arg_value argument.
    
    @ Description: This method is used for calculating value of a function in certain point (specified by arg_value).
    Function_choice is a number representing certain function in menu.
"""


def calculate_function_value(function_choice, arg_value):
    value = 0
    match function_choice:
        case 1:
            value = 0.6 * arg_value - 1.3
        case 2:
            value = 2.1 * abs(arg_value) - 3.0
        case 3:
            value = 3 * math.sin(2 * arg_value) - 0.5
        case 4:
            value = calculate_horner_scheme(4, [1, -3, 1, -7], arg_value)
        case 5:
            value = calculate_horner_scheme(4, [1, -3, 1, -7], abs(arg_value))
        case 6:
            value = 1.5 * math.cos(abs(2 * arg_value)) - 0.25
        case 7:
            value = 0.75 * abs(math.sin(0.5 * arg_value))
        case 8:
            value = calculate_horner_scheme(4, [1, -3, 1, -7], math.sin(2 * arg_value))
        case 9:
            value = math.sin(arg_value) + 2 * arg_value + 5
        case 10:
            value = 2.1 * math.sin(calculate_horner_scheme(4, [1, -3, 1, -7], arg_value))
        case 11:
            value = 2 * math.sin(3 * arg_value) + math.cos(3 * arg_value)
        case 12:
            value = pow(arg_value, 3) + math.cos(arg_value)
    return value


"""
    @ Function: calculate_chebyshev_polynomial_value()
    
    @ Parameters:
    
    * arg_value         -> argument value, which Chebyshev polynomial value will be calculated for.
    * polynomial_degree -> degree of a Chebyshev polynomial (used for getting value of a correct polynomial).
    
    @ Returns: Value of a Chebyshev polynomial of polynomial_degree degree for arg_value argument.
    
    @ Description: This method is used for calculating value of any Chebyshev polynomial value for any given
    argument.
"""


def calculate_chebyshev_polynomial_value(arg_value, polynomial_degree):
    if polynomial_degree == 0:
        return 1
    elif polynomial_degree == 1:
        return arg_value
    else:
        degree_minus_two = 1
        degree_minus_one = arg_value
        for i in range(2, polynomial_degree + 1):
            temp = degree_minus_one
            degree_minus_one = 2 * arg_value * degree_minus_one - degree_minus_two
            degree_minus_two = temp
        return degree_minus_one


"""
    @ Function: calculate_legendre_polynomial_value()

    @ Parameters:

    * arg_value         -> argument value, which Legendre polynomial value will be calculated for.
    * polynomial_degree -> degree of a Legendre polynomial (used for getting value of a correct polynomial).

    @ Returns: Value of a Legendre polynomial of polynomial_degree degree for arg_value argument.

    @ Description: This method is used for calculating value of any Legendre polynomial value for any given
    argument.
"""


def calculate_legendre_polynomial_value(arg_value, polynomial_degree):
    if polynomial_degree == 0:
        return 1
    elif polynomial_degree == 1:
        return arg_value
    else:
        degree_minus_two = 1
        degree_minus_one = arg_value
        for i in range(2, polynomial_degree + 1):
            temp = degree_minus_one
            degree_minus_one = ((2 * i - 1) * arg_value * degree_minus_one - (i - 1) * degree_minus_two) / i
            degree_minus_two = temp
        return degree_minus_one


"""
    @ Function: calculate_hermite_polynomial_value()

    @ Parameters:

    * arg_value         -> argument value, which Hermite polynomial value will be calculated for.
    * polynomial_degree -> degree of a Hermite polynomial (used for getting value of a correct polynomial).

    @ Returns: Value of a Hermite polynomial of polynomial_degree degree for arg_value argument.

    @ Description: This method is used for calculating value of any Hermite polynomial value for any given
    argument.
"""


def calculate_hermite_polynomial_value(arg_value, polynomial_degree):
    if polynomial_degree == 0:
        return 1
    elif polynomial_degree == 1:
        return 2 * arg_value
    else:
        degree_minus_two = 1
        degree_minus_one = 2 * arg_value
        for i in range(2, polynomial_degree + 1):
            temp = degree_minus_one
            degree_minus_one = 2 * arg_value * degree_minus_one - 2 * (i - 1) * degree_minus_two
            degree_minus_two = temp
        return degree_minus_one


"""
    @ Function: calculate_laugerre_polynomial_value()

    @ Parameters:

    * arg_value         -> argument value, which Laugerre polynomial value will be calculated for.
    * polynomial_degree -> degree of a Laugerre polynomial (used for getting value of a correct polynomial).

    @ Returns: Value of a Laugerre polynomial of polynomial_degree degree for arg_value argument.

    @ Description: This method is used for calculating value of any Laugerre polynomial value for any given
    argument.
"""


def calculate_laugerre_polynomial_value(arg_value, polynomial_degree):
    if polynomial_degree == 0:
        return 1
    elif polynomial_degree == 1:
        return arg_value - 1
    else:
        degree_minus_two = 1
        degree_minus_one = arg_value - 1
        for i in range(2, polynomial_degree + 1):
            temp = degree_minus_one
            degree_minus_one = (arg_value - 2 * i + 1) * degree_minus_one - pow(i - 1, 2) * degree_minus_two
            degree_minus_two = temp
        return degree_minus_one


"""
    @ Function: weight_function_for_chebyshev()
    
    @ Parameters:
    
    * arg_value -> argument value, which weight function value will be calculated for.
    
    @ Returns: Value of weight function for a given argument.
    
    @ Description: This function is used for calculating weight function value for Chebyshev polynomial for any
    given argument.
"""


def weight_function_for_chebyshev(arg_value):
    return 1 / math.sqrt(1 - pow(arg_value, 2))


"""
    @ Function: weight_function_for_chebyshev()
    
    @ Parameters:
    
    * arg_value -> argument value, which weight function value will be calculated for.
    
    @ Returns: Value of weight function for a given argument.
    
    @ Description: This function is used for calculating weight function value for Hermite polynomial for any
    given argument.
"""


def weight_function_for_hermite(arg_value):
    return pow(math.e, -1 * pow(arg_value, 2))


"""
    @ Function: weight_function_for_chebyshev()
    
    @ Parameters:
    
    * arg_value -> argument value, which weight function value will be calculated for.
    
    @ Returns: Value of weight function for a given argument.
    
    @ Description: This function is used for calculating weight function value for Laugerre polynomial for any
    given argument.
"""


def weight_function_for_laguerre(arg_value):
    return pow(math.e, -arg_value)


"""
    @ Function:
    
    @ Parameters:
    
    @ Returns:
    
    @ Description:
"""


def calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side, variant, degree, up):
    number_of_intervals = 1
    previous_integral_value = calculate_integral_simpson_method(function_choice, number_of_intervals, left_side, right_side, variant, degree, up)
    number_of_intervals *= 2
    integral_value = calculate_integral_simpson_method(function_choice, number_of_intervals, left_side, right_side, variant, degree, up)
    while abs(integral_value - previous_integral_value) >= epsilon:
        previous_integral_value = integral_value
        number_of_intervals *= 2
        integral_value = calculate_integral_simpson_method(function_choice, number_of_intervals, left_side, right_side, variant, degree, up)
    return integral_value


"""
    @ Function:

    @ Parameters:

    @ Returns:

    @ Description:
"""


def calculate_integral_simpson_method(function_choice, number_of_intervals, left_side, right_side, variant, degree, up):
    # left_side = recalculate_value(left_side, left_side, right_side, variant)
    # right_side = recalculate_value(right_side, left_side, right_side, variant)
    interval_length = abs(right_side - left_side)
    sub_interval_length = interval_length / number_of_intervals
    integral_value = 0
    if up:
        for i in range(0, number_of_intervals):
            a = left_side + i * sub_interval_length
            b = a + sub_interval_length
            integral_value += ((b - a) / 6) * (calculate_function_value(function_choice, a) * get_weight_function_value(variant, a) * get_polynomial_value(a, variant, degree)
                + 4 * calculate_function_value(function_choice, (a + b) / 2) * get_weight_function_value(variant, (a + b) / 2) * get_polynomial_value((a + b) / 2, variant, degree)
                + calculate_function_value(function_choice, b) * get_weight_function_value(variant, b) * get_polynomial_value(b, variant, degree))
    else:
        for i in range(0, number_of_intervals):
            a = left_side + i * sub_interval_length
            b = a + sub_interval_length
            integral_value += ((b - a) / 6) * (get_weight_function_value(variant, a) * pow(get_polynomial_value(a, variant, degree), 2)
                + 4 * get_weight_function_value(variant, (a + b) / 2) * pow(get_polynomial_value((a + b) / 2, variant, degree), 2)
                + get_weight_function_value(variant, b) * pow(get_polynomial_value(b, variant, degree), 2))
    return integral_value


"""
    @ Function:

    @ Parameters:

    @ Returns:

    @ Description:
"""


def get_limit_value_for_newton_cotes(function_choice, epsilon, f_left_side, f_right_side, variant, degree, up):
    left_side = 0
    delta = 1
    actual_integral_value = 0
    if f_right_side > 1:
        right_side = left_side + delta
        integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side, variant, degree, up)
        actual_integral_value = integral_iteration_value
        while abs(integral_iteration_value) >= epsilon:
            left_side = right_side
            right_side += delta
            integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side, variant, degree, up)
            actual_integral_value += integral_iteration_value
    elif 0 < f_right_side <= 1:
        right_side = 0.5
        integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side, variant, degree, up)
        actual_integral_value = integral_iteration_value
        iteration_number = 0
        while abs(integral_iteration_value) >= epsilon:
            iteration_number += 1
            left_side = right_side
            right_side += 0.5 * math.pow(0.5, iteration_number)
            integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side, variant, degree, up)
            actual_integral_value += integral_iteration_value
    right_side = 0
    if f_left_side < -1:
        left_side = right_side - delta
        integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side, variant, degree, up)
        actual_integral_value += integral_iteration_value
        while abs(integral_iteration_value) >= epsilon:
            right_side = left_side
            left_side -= delta
            integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side, variant, degree, up)
            actual_integral_value += integral_iteration_value
    elif -1 <= f_left_side < 0:
        left_side = -0.5
        integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side, variant, degree, up)
        actual_integral_value += integral_iteration_value
        iteration_number = 0
        while abs(integral_iteration_value) >= epsilon:
            iteration_number += 1
            right_side = left_side
            left_side += -0.5 * math.pow(0.5, iteration_number)
            integral_iteration_value = calculate_definite_integral_newton_cotes(function_choice, epsilon, left_side, right_side, variant, degree, up)
            actual_integral_value += integral_iteration_value
    return actual_integral_value


"""
    @ Function:

    @ Parameters:

    @ Returns:

    @ Description:
"""


def get_polynomial_value(arg_value, variant, degree):
    value = 0
    match variant:
        case 1:
            value = calculate_chebyshev_polynomial_value(arg_value, degree)
        case 2:
            value = calculate_hermite_polynomial_value(arg_value, degree)
        case 3:
            value = calculate_laugerre_polynomial_value(arg_value, degree)
        case 4:
            value = calculate_legendre_polynomial_value(arg_value, degree)
    return value


"""
    @ Function:

    @ Parameters:

    @ Returns:

    @ Description:
"""


def get_weight_function_value(variant, arg_value):
    value = 1
    match variant:
        case 1:
            value = weight_function_for_chebyshev(arg_value)
        case 2:
            value = weight_function_for_hermite(arg_value)
        case 3:
            value = weight_function_for_laguerre(arg_value)
        case 4:
            value = 1
    return value


"""
    @ Function:

    @ Parameters:

    @ Returns:

    @ Description:
"""


def approxmiate_given_function(function_choice, left_side, right_side, integration_epsilon, mode_choice, mode_value, variant):
    iteration_value = -1
    list_of_coefficients = []
    if mode_choice == "1":
        iteration_value = mode_value
        for i in range(0, mode_value):
            up = get_limit_value_for_newton_cotes(function_choice, integration_epsilon, left_side, right_side, variant, i, True)
            down = get_limit_value_for_newton_cotes(function_choice, integration_epsilon, left_side, right_side, variant, i, False)
            coefficient_value = up / down
            list_of_coefficients.append(coefficient_value)
        error_value = calculate_error_value(list_of_coefficients, variant, function_choice, left_side, right_side)
    else:
        error_value = 0
        while error_value > mode_value or iteration_value == -1:
            iteration_value += 1
            list_of_coefficients.clear()
            for i in range(0, iteration_value):
                up = get_limit_value_for_newton_cotes(function_choice, integration_epsilon, left_side, right_side, variant, i, True)
                down = get_limit_value_for_newton_cotes(function_choice, integration_epsilon, left_side, right_side, variant, i, False)
                coefficient_value = up / down
                list_of_coefficients.append(coefficient_value)
            error_value = calculate_error_value(list_of_coefficients, variant, function_choice, left_side, right_side)
    make_graphs(left_side, right_side, function_choice, list_of_coefficients, variant)
    return [error_value, iteration_value]


"""
    @ Function:

    @ Parameters:

    @ Returns:

    @ Description:
"""


def calculate_error_value(list_of_coefficients, variant, function_choice, left_side, right_side):
    point_value = left_side
    maximum = 0
    while point_value <= right_side:
        function_value = calculate_function_value(function_choice, point_value)
        approximate_value = 0
        for i in range(len(list_of_coefficients)):
            new_point = recalculate_value(point_value, left_side, right_side, variant)
            approximate_value += list_of_coefficients[i] * get_polynomial_value(new_point, variant, i)
        if abs(function_value - approximate_value) > maximum:
            maximum = abs(function_value - approximate_value)
        point_value = point_value + 0.01
    return maximum


"""
    @ Function:

    @ Parameters:

    @ Returns:

    @ Description:
"""


def make_graphs(left_side, right_side, function_choice, list_of_coefficients, variant):
    array_of_points = np.linspace(left_side, right_side, 500)
    function_values = []
    approximate_values = []
    for point in array_of_points:
        function_values.append(calculate_function_value(function_choice, point))
    for point in array_of_points:
        approximate_value = 0
        new_point = recalculate_value(point, left_side, right_side, variant)
        for i in range(len(list_of_coefficients)):
            approximate_value += list_of_coefficients[i] * get_polynomial_value(new_point, variant, i)
        approximate_values.append(approximate_value)

    plt.subplots(1, 1, figsize=(10, 14))
    plt.plot(array_of_points, function_values, color="green")
    plt.plot(array_of_points, approximate_values, color="orange", linestyle="dashed")
    distance = abs(right_side - left_side) / 10
    plt.xlim((left_side - (distance / 10), right_side + (distance / 10)))
    plt.ylim((-10.1, 10.1))
    plt.xticks(np.arange(left_side, right_side + (distance / 10), step=distance))
    plt.yticks(np.arange(-10.0, 10.1, step=1.00))
    plt.yticks(np.arange(-10.0, 10.1, step=0.25), minor=True)
    plt.xlabel("Oś OX")
    plt.ylabel("Oś OY")
    plt.title("Porównanie wybranej funkcji oraz funkcji aproksymującej")
    plt.grid()
    plt.legend(["Funkcja oryginalna", "Wielomian aproksymujący"])

    plt.show()


def recalculate_value(arg_value, left_side, right_side, variant):
    value = 0
    match variant:
        case 1:
            value = (2 * arg_value - left_side - right_side) / (right_side - left_side)
        case 2:
            value = arg_value
        case 3:
            value = arg_value
        case 4:
            value = (2 * arg_value - left_side - right_side) / (right_side - left_side)
    return value