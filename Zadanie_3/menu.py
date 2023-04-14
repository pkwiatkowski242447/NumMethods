import additional as ad
import calc as cl

"""
    @ Function: main_header()

    @ Parameters: None

    @ Description: this function is used for printing character sequence, containing the subject's title,
    number of the exercise and the topic of the exercise.
"""


def main_header():
    print("=====================================================")
    print("===== Metody numeryczne - zadanie: interpolacja =====")
    print("=====================================================")


"""
    @ Function: starting_menu()

    @ Parameters: None

    @ Description: this function is used for printing character sequence, containing text menu for 
    this program functionalities
"""


def starting_menu():
    print("==================== Główne menu ====================")
    print("1. Wybór funkcji do interpolowania.")
    print("2. Zakończenie działania programu.")
    print("=====================================================")


"""
    @ Function: function_choice_menu()

    @ Parameters: None

    @ Description: this function is used for printing character sequence, containing a list of function, that 
    can be interpolated.
    
"""


def function_choice_menu():
    print("================ Menu wyboru funkcji ================")
    print("1. 2.3 x + 0.5")
    print("2. 2 * |x| - 2.5")
    print("3. sin(x)")
    print("4. x ^ 2 + x + 4")
    print("5. cos(7x + 6)")
    print("6. 8.1 sin(x) + x")
    print("7. (sin 2x) ^ 3 - 1")
    print("8. cos |x| - 2")
    print("9. |sin x| + cos|x|")
    print("10. |x| ^ 3 - 2 * |x| + 8")
    print("11. Powrót do poprzedniego menu.")
    print("=====================================================")


"""
    @ Function: get_function_string()
    
    @ Parameters:
    
    * function_choice -> number of a function chosen by the user from menu.
    
    @ Description: This method is used for retrieving string representing original function's
    formula.
"""


def get_function_string(function_choice):
    function_formula = ""
    match function_choice:
        case 1:
            function_formula = "2.3 x + 0.5"
        case 2:
            function_formula = "2 * |x| - 2.5"
        case 3:
            function_formula = "sin(x)"
        case 4:
            function_formula = "x ^ 2 + x + 4"
        case 5:
            function_formula = "cos(7x + 6)"
        case 6:
            function_formula = "8.1 sin(x) + x"
        case 7:
            function_formula = "(sin 2x) ^ 3 - 1"
        case 8:
            function_formula = "cos |x| - 2"
        case 9:
            function_formula = "|sin x| + cos|x|"
        case 10:
            function_formula = "|x| ^ 3 - 2 * |x| + 8"
    return function_formula


"""
    @ Function: values_insert_menu() 
    
    @ Parameters: None
    
    @ Description: this method is used for display the user menu containing ways, in which they can insert
    function values, used for interpolation.
"""


def values_insert_menu():
    print("== Wprowadzadzanie wartości funkcji interpolowanej ==")
    print("1. Wprowadzanie wartości ręcznie, przez użytkownika.")
    print("2. Wczytywanie wartości funkcji z pliku.")
    print("=====================================================")


"""
    @ Function: interactive_value_insertion() 

    @ Parameters: 
    
    * start_of_interval -> the start of interval, where argument values are located
    * end_of_interval   -> the end of interval, where argument values are located

    @ Description: this method is used for display the user menu containing ways, in which they can insert
    function values, used for interpolation.
"""


def interactive_value_insertion(start_of_interval, end_of_interval, function_choice, initial_dict):
    insert_new_value = 1
    dictionary_of_arguments = initial_dict
    while insert_new_value != 4:
        print("Wartości funkcji: ")
        for i in dictionary_of_arguments:
            if len(dictionary_of_arguments) != 0:
                print("* F(" + "{:.4f}".format(i) + ") = " + "{:.4f}".format(dictionary_of_arguments[i]))
            else:
                ad.print_new_line()
                print("Wartości funkcji: ")
                print("BRAK")
        ad.print_new_line()
        print("== Wprowadzadzanie wartości funkcji interpolowanej ==")
        print("1. Dodanie kolejnej wartości funkcji.")
        print("2. Usunięcie dodanej wartości funkcji.")
        print("3. Usunięcie wszystkich dodanych wartości funkcji.")
        print("4. Koniec")
        print("=====================================================")
        insert_new_value = int(input("Twój wybór: "))
        ad.print_new_line()
        if insert_new_value == 1:
            arg_value = float(input("Podaj wartość argumentu: "))
            if start_of_interval <= arg_value <= end_of_interval:
                function_val = cl.calculate_function_value(arg_value, function_choice)
                dictionary_of_arguments[arg_value] = function_val
            else:
                ad.print_new_line()
                print("Podana wartość argumentu jest spoza przedziału interpolacji.")
                ad.press_to_continue()
        elif insert_new_value == 2:
            arg_value = float(input("Podaj wartość argumentu: "))
            del dictionary_of_arguments[arg_value]
        elif insert_new_value == 3:
            dictionary_of_arguments = {}
        ad.clear_screen()
    return dictionary_of_arguments