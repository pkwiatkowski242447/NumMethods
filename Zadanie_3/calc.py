import math


def function_value(x, function_choice):
    coeff_function_4 = [1, 1, 4]
    coeff_function_7 = [1, 0, 0, -1]
    coeff_function_10 = [1, -2, 8]
    match function_choice:
        case 1:
            y_value = 2.3 * x + 0.5
        case 2:
            y_value = 2 * abs(x) - 2.5
        case 3:
            y_value = math.sin(x)
        case 4:
            y_value = horner_scheme(x, coeff_function_4, 3)
        case 5:
            y_value = math.cos(7 * x + 6)
        case 6:
            y_value = 8.1 * math.sin(x) + x
        case 7:
            y_value = horner_scheme(math.sin(2 * x), coeff_function_7, 4)
        case 8:
            y_value = math.cos(abs(x)) - 2
        case 9:
            y_value = abs(math.sin(x)) + abs(math.cos(x))
        case 10:
            y_value = horner_scheme(abs(x), coeff_function_10, 3)
        case _:
            y_value = 0
    return y_value


def horner_scheme(arg, array, num):
    itr = 0
    temp = array[itr]
    while itr < num - 1:
        temp = temp * arg + array[itr + 1]
        itr += 1
    return temp
