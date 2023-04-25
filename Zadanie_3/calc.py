import math
import numpy as np
import matplotlib.pyplot as plt
import menu as mn


"""
    @ Function: horner_scheme()
    
    @Parameters:
    
    * argument_value         -> value of the argument, for which value of a selected function will be calculated
    * array_of_coefficients  -> array of coefficients standing right to next powers of x (where powers are in descending
    order)
    * number_of_coefficients -> total number of coefficients in array (even if some are zeros) 
"""


def horner_scheme(argument_value, array_of_coefficients, number_of_coefficients):
    function_value = 0
    for i in range(number_of_coefficients):
        function_value = function_value * argument_value + array_of_coefficients[i]
    return function_value


"""
    @ Function: calculate_function_value() 
    
    @ Parameters: 
    
    * function_arg      -> argument, which value will be calculated for
    * function_choice   -> numerical identifier of chosen function to interpolate
    
    @ Description: function that is used to calculate function value for a given argument
"""


def calculate_function_value(function_arg, function_choice):
    function_val = 0
    match function_choice:
        case 1:
            function_val = 2.3 * function_arg + 0.5
        case 2:
            function_val = 2 * abs(function_arg) - 2.5
        case 3:
            function_val = math.sin(function_arg)
        case 4:
            function_val = horner_scheme(function_arg, [1, 1, 4], 3)
        case 5:
            function_val = math.cos(7 * function_arg + 6)
        case 6:
            function_val = 8.1 * math.sin(function_arg) + function_arg
        case 7:
            function_val = horner_scheme(math.sin(3 * function_arg), [1, 0, 0, -1], 4)
        case 8:
            function_val = math.cos(abs(function_arg)) - 2
        case 9:
            function_val = abs(math.sin(function_arg)) + math.cos(abs(function_arg))
        case 10:
            function_val = horner_scheme(abs(function_arg), [1, -2, 8], 3)
    return function_val


"""
    @ Function: interpolate_chosen_function()
    
    @ Parameters:
    
    * start_of_interval -> start of the interpolation interval, used for making graphs
    * end_of_interval   -> end of the interpolation interval, used for making graphs
    * function_choice   -> numerical identifier of function chosen by the user
    * dict_of_values    -> dictionary containing pairs argument value -> function value for that argument
    
    @ Description: this method does construct interpolation polynomial, and then calls function responsible for
    making graph for both interpolated and interpolation functions - overlaps them and marks their overlapping points
"""


# TODO: write implementation of the function below and function responsible for
#  making graphs of functions (it should take as params stand and end of interval and based on that take the scale)


def interpolate_chosen_function(start_of_interval, end_of_interval, function_choice, dict_of_values):
    list_of_args = list(dict_of_values.keys())
    list_of_vals = list(dict_of_values.values())
    returned_array = divided_difference_table(list_of_args, list_of_vals)[0, :]
    make_functions_plot(function_choice, returned_array, mn.get_function_string(function_choice), start_of_interval,
                        end_of_interval, list_of_args, list_of_vals)


"""
    @ Function: divided_difference_table()

    @ Parameters:

    * list_of_args -> List containing all of arguments, which divided differences will be calculated for.
    * list_of_vals -> List of values of a function for given arguments, that will be used for calculating
    divided differences.

    @ Description: This function is used for getting divided differences table, used later 
    for calculating Newton's polynomial.
"""


def divided_difference_table(list_of_args, list_of_vals):
    number_of_rows = len(list_of_vals)
    coefficients = np.zeros([number_of_rows, number_of_rows])
    coefficients[:, 0] = list_of_vals
    for j in range(1, number_of_rows):
        for i in range(number_of_rows - j):
            coefficients[i][j] = (
                        (coefficients[i + 1][j - 1] - coefficients[i][j - 1]) / (list_of_args[i + j] - list_of_args[i]))
    return coefficients


"""
    @ Function: calculate_polynomial_value()
    
    @ Parameters: 
    
    * coefficients -> array containing values of divided differences
    * list_of_args -> array containing values of arguments with known values
    * current_arg  -> value of argument, which chosen function is interpolated for
    
    @ Description: This function is used for calculating interpolation function value for a given argument.
"""


def calculate_polynomial_value(coefficients, list_of_args, current_arg):
    length_of_args = len(list_of_args) - 1
    polynomial_value = coefficients[length_of_args]
    for i in range(1, length_of_args + 1):
        polynomial_value = coefficients[length_of_args - i] + (current_arg - list_of_args[length_of_args - i]) * polynomial_value
    return polynomial_value


"""
    @ Function: make_functions_plot()
    
    @ Parameters: 
    
    * function_choice               -> number of a function chosen from the menu by the user
    * array_of_itr_coefficients     -> array of coefficients in the interpolating function's formula - used for
    calculating interpolating function's values.
    * org_formula                   -> string representing original function's formula
    * start_of_interval             -> start of original function's arguments interval
    * end_of_interval               -> end of original function's arguments interval
    * list_of_known_args            -> list containing arguments of a function, specified by the user
    * list_of_known_vals            -> list containing values for user specified arguments
    
    @ Description: This method is used for making plot with both original and interpolating function
    in order to compare them and show them to the user.
"""


def make_functions_plot(function_choice, array_of_itr_coefficients, org_formula, start_of_interval,
                        end_of_interval, list_of_known_args, list_of_known_vals):
    list_of_points = np.linspace(start_of_interval, end_of_interval, int(end_of_interval - start_of_interval) * 1000)
    list_of_values_org = []
    list_of_values_itr = []

    for i in list_of_points:
        list_of_values_org.append(calculate_function_value(i, function_choice))

    for i in list_of_points:
        list_of_values_itr.append(calculate_polynomial_value(array_of_itr_coefficients, list_of_known_args, i))

    plt.subplots(1, 1, figsize=(10, 14))
    plt.plot(list_of_points, list_of_values_org, color="green")
    plt.plot(list_of_points, list_of_values_itr, color="orange", linestyle="dashed")
    plt.scatter(list_of_known_args, list_of_known_vals, marker='X', color="blue")
    distance = abs(end_of_interval - start_of_interval) / 10
    plt.xlim((start_of_interval - (distance / 10), end_of_interval + (distance / 10)))
    plt.ylim((-20.1, 20.1))
    plt.xticks(np.arange(start_of_interval, end_of_interval + (distance / 10), step=distance))
    plt.yticks(np.arange(-20.1, 20.1, step=2.5))
    plt.xlabel("Oś OX")
    plt.ylabel("Oś OY")
    plt.title("Porównanie wybranej funkcji oraz funkcji interpolującej")
    plt.grid()
    plt.legend(["Funkcja oryginalna", "Wielomian interpolujący", "Węzły interpolacji"])

    plt.show()
