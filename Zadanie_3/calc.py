import math

import pandas as pd

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
            function_val = 8.1 * function_arg + 2.5
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
    @ Function: calculate_interpolation_polynomial()
    
    @ Parameters:
    
    * function_choice   -> numerical identifier of function chosen by the user
    * dict_of_values    -> dictionary containing pairs argument value -> function value for that argument
    
    @ Description: this method does construct interpolation polynomial, and then calls function responsible for
    making graph for both interpolated and interpolation functions - overlaps them and marks their overlapping points
"""


# TODO: write implementation of the function below and function responsible for
#  making graphs of functions (it should take as params stand and end of interval and based on that take the scale)


def calculate_interpolation_polynomial(start_of_interval, end_of_interval, function_choice, dict_of_values):
    return 0
