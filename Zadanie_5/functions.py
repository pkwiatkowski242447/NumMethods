import math


def function_value(function_choice, x):
    if function_choice == "linear":
        return x
    elif function_choice == "absolute":
        return abs(x)
    elif function_choice == "polynomial":
        return x ** 2 - 3 * x + 2
    elif function_choice == "trigonometric":
        return math.sin(x)
    elif function_choice == "composite":
        return abs(math.sin(x))
