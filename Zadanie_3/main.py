import calc as cl
import menu as mn
import additional as ad

"""
    Main function of the program - it contains all required operation
    to interpolate a certain function, selected by the user from the function menu.
"""


def main():
    ad.clear_screen()
    functionality_choice = 1
    while functionality_choice != 2:
        mn.main_header()
        ad.print_new_line()
        mn.starting_menu()
        functionality_choice = int(input("Twój wybór: "))
        if functionality_choice == 1:
            ad.clear_screen()
            mn.main_header()
            ad.print_new_line()
            mn.function_choice_menu()
            function_choice = int(input("Twój wybór: "))
            if function_choice != 11:
                ad.print_new_line()
                start_of_interval = float(input("Podaj początek przedziału, w którym wybrana funkcja ma być interpolowana: "))
                end_of_interval = float(input("Podaj koniec przedziału, w którym wybrana funkcja ma być interpolowana: "))
                ad.print_new_line()
                mn.values_insert_menu()
                insert_values = int(input("Twój wybór: "))
                dict_of_values = {}
                if insert_values == 2:
                    ad.print_new_line()
                    file_name = input("Podaj nazwę pliku z argumentami funkcji: ")
                    list_of_args = ad.read_function_args(file_name)
                    dict_of_values = {}
                    for i in range(len(list_of_args)):
                        if start_of_interval <= list_of_args[i] <= end_of_interval:
                            function_val = cl.calculate_function_value(list_of_args[i], function_choice)
                            dict_of_values[list_of_args[i]] = function_val
                    ad.clear_screen()
                    dict_of_values = mn.interactive_value_insertion(start_of_interval, end_of_interval, function_choice, dict_of_values)
                    ad.press_to_continue()
                else:
                    ad.clear_screen()
                    dict_of_values = mn.interactive_value_insertion(start_of_interval, end_of_interval, function_choice, {})
                    ad.press_to_continue()
                cl.calculate_interpolation_polynomial(start_of_interval, end_of_interval, function_choice, dict_of_values)
        else:
            ad.clear_screen()
            print("Wybrano zakończenie działania programu.")
            ad.press_to_continue()
        ad.clear_screen()


if __name__ == "__main__":
    main()
