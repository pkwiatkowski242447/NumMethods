import additional as ad
import menu as mn
import calc as cl

"""
    @ Function: main()
    
    @ Parameters: Nones
    
    @ Returns: void
    
    @ Description: This method is responsible for performing all required operations in the task. Specifically, it is
    designed to get user input in order to navigate menus and after choosing some options (accordinlgy to specific menu)
    the result will be shown (this time it will be a graph of a base function - which can by a linear, trygonometric 
    or |x| function or polynomial and their combinations - and a function that does approximate the values of the original 
    function - this one is typically polynomial), and after that approximation error is calculated.
"""


def main():
    user_choice = 0
    while user_choice != "2":
        ad.clear_screen()
        mn.print_main_menu()
        user_choice = input("Twój wybór: ")
        ad.print_new_line()
        match user_choice:
            case "1":
                mn.function_choice_menu()
                function_choice = int(input("Twój wybór: "))
                ad.print_new_line()
                left_side = float(input("Podaj lewą krawędź przedziału aproksymacji: "))
                right_side = float(input("Podaj prawą krawędź przedziału aproksymacji: "))
                ad.print_new_line()
                intergration_epsilon = float(input("Podaj dokładność całkowania (kwadraturą Newtona - Cotesa): "))
                ad.print_new_line()
                mode_value = 0
                mode_choice = 0
                while mode_choice != "1" and mode_choice != "2":
                    mn.program_mode_menu()
                    mode_choice = input("Twój wybór: ")
                    match mode_choice:
                        case "1":
                            ad.print_new_line()
                            mode_value = int(input("Podaj stopień wielomianu aproksymjuącego: "))
                        case "2":
                            ad.print_new_line()
                            mode_value = float(input("Podaj oczekiwaną wartość błędu aproksymacji: "))
                        case other:
                            ad.print_new_line()
                            print("Wybrano nieprawidłowy typ pracy programu.")
                            ad.press_to_continue()
                ad.print_new_line()
                mn.variant_choice_menu()
                variant = int(input("Twój wybór: "))
                ad.print_new_line()
                approxmiation_error = cl.approxmiate_given_function(function_choice, left_side, right_side, intergration_epsilon, mode_choice, mode_value, variant)
                ad.print_new_line()
                print("Uzyskany błąd aproksymacji: " + "{:.10f}".format(approxmiation_error))
            case "2":
                ad.print_new_line()
                print("Wybrano zakończenie programu.")
                ad.print_new_line()
                ad.press_to_continue()
            case other:
                ad.print_new_line()
                print("Wybrano nieprawidłową opcję (spoza menu).")
                ad.print_new_line()
                ad.press_to_continue()


if __name__ == "__main__":
    main()
