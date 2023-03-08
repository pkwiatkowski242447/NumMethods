import addon as ad
import math


def function_value(arg, function_choice):
    coefficients = [1, 2, 0, 7]
    match function_choice:
        case 1:
            val = horner_scheme(arg, coefficients, 4)
        case 2:
            val = math.cos(arg)
        case 3:
            val = math.e ** arg     # Ewentualnie tu zmiana w operatorze **
        case 4:
            val = horner_scheme(math.cos(arg), coefficients, 4)
        case 5:
            val = math.cos(horner_scheme(arg, coefficients, 4))
        case 6:
            val = math.e ** math.cos(arg)
        case 7:
            val = math.cos(math.e ** arg)
        case 8:
            val = horner_scheme(math.e ** arg, coefficients, 4)
        case 9:
            val = math.e ** horner_scheme(arg, coefficients, 4)
        case _:
            val = 0
    return val


def horner_scheme(arg, array, num):
    itr = 0
    temp = array[itr]
    while itr < num - 1:
        temp = temp * arg + array[itr + 1]
        itr += 1
    return temp

# bisection - znaleznienie miejsca zerowego za pomocą metody bisekcji
# secant_method - znalezienie miejsca zerowego za pomocą metody siecznych

# function_number   -> oznacza numer wybranej przez użytkownika funkcji
# start             -> oznacza początek przedziału, w którym poszukiwane będzie miejsce zerowe
# end               -> oznacza koniec przedziału, w którym poszukiwane będzie miejsce zerowe
# cond              -> oznacza warunek stopu
# value             -> oznacza wartość eps, przy warunku na dokładność lub też liczby iteracji, przy warunku na liczbę iteracji


def bisection(function_number, start, end, cond, value):
    value_a = function_value(start, function_number)
    value_b = function_value(end, function_number)
    mid = (start + end) / 2
    itr = 0
    temp = 0
    if value_a * value_b > 0:
        print("\nWartości funcji na końcach przedziałów są tego samego znaku, przez co wymagania bisekcji nie są spełnione.")
    else:
        if value_a * value_b == 0:
            if value_a == 0:
                return start, 0
            else:
                return end, 0
        if cond == 1:
            while abs(mid - temp) > value:
                temp = mid
                value_mid = function_value(mid, function_number)
                itr += 1
                if value_mid == 0:
                    return mid, itr
                elif value_a * value_mid < 0:
                    end = mid
                    value_b = value_mid
                elif value_b * value_mid < 0:
                    start = mid
                    value_a = value_mid
                mid = (start + end) / 2
            print("\nMiejscem zerowym wybranej funkcji jest x = " + str(mid) + ", wyznaczony bisekcją.")
            print("Uzykana liczba iteracji: " + str(itr))
            return mid
        else:
            for i in range(value + 1):
                temp = mid
                mid = (start + end) / 2
                value_mid = function_value(mid, function_number)
                if value_mid == 0:
                    return mid, (end - start)
                elif value_a * value_mid < 0:
                    end = mid
                    value_b = value_mid
                elif value_b * value_mid < 0:
                    start = mid
                    value_a = value_mid
            print("\nMiejscem zerowym wybranej funkcji jest x = " + str(mid) + ", wyznaczony bisekcją.")
            print("Uzykana dokładność wyznaczenia miejsca zerowego: " + str(mid - temp))
            return mid


def secant_method(function_number, x1, x2, cond, value):
    start_x1 = x1
    start_x2 = x2
    value_x1 = function_value(x1, function_number)
    value_x2 = function_value(x2, function_number)
    itr = 0
    if value_x1 * value_x2 > 0:
        print("\nWartości funcji na końcach przedziałów są tego samego znaku, przez co wymagania metody siecznych nie są spełnione.")
    else:
        if cond == 1:
            while abs(x2 - x1) > value:
                itr += 1
                if value_x2 - value_x1 != 0:
                    next_one = x2 - ((value_x2 * (x2 - x1)) / (value_x2 - value_x1))
                    next_val = function_value(next_one, function_number)
                    x1 = x2
                    value_x1 = value_x2
                    x2 = next_one
                    value_x2 = next_val
            if x2 < start_x1 or x2 > start_x2:
                print("\nNie udało się wyznaczyć miejsca zerowego wybranej funkcji.")
            else:
                print("\nPierwiastkiem wybranej funkcji jest x = " + str(x2) + ", wyznaczony metodą siecznych.")
                print("Uzyskana liczba iteracji: " + str(itr))
                return x2
        else:
            while itr <= value:
                itr += 1
                if value_x2 - value_x1 != 0:
                    next_one = x2 - ((value_x2 * (x2 - x1)) / (value_x2 - value_x1))
                    next_val = function_value(next_one, function_number)
                    x1 = x2
                    value_x1 = value_x2
                    x2 = next_one
                    value_x2 = next_val
            if x2 < start_x1 or x2 > start_x2:
                print("\nNie udało się wyznaczyć miejsca zerowego wybranej funkcji.")
            else:
                print("\nPierwiastkiem wybranej funkcji jest x = " + str(x2) + ", wyznaczony metodą siecznych.")
                print("Uzyskana dokładność wyznaczenia miejsca zerowego: " + str(x2 - x1))
                return x2
