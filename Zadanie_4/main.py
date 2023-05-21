import menu as mn
import additional as ad


def main():
    choice = 0
    while choice != "3":
        ad.clear_screen()
        mn.print_main_menu()
        choice = input("Podaj twój wybór: ")
        ad.print_new_line()
        match choice:
            case "1":
                integral_value = mn.print_newton_cotes_menu()
                ad.print_new_line()
                print("Wartość całki oznaczonej wybranej funkcji na przedziale [-1, 1]: " + '{:.12}'.format(integral_value))
                ad.print_new_line()
                ad.press_to_continue()
            case "2":
                integral_value = mn.print_gauss_menu()
                ad.print_new_line()
                print("Wartość całki oznaczonej wybranej funkcji na przedziale [-1, 1]: " + '{:.12}'.format(integral_value))
                ad.print_new_line()
                ad.press_to_continue()p
            case "3":
                print("Wybrano zakończenie programu.")
                ad.print_new_line()
                ad.press_to_continue()
            case other:
                print("Wybrano opcję, która nie znajduje się w menu.")
                ad.print_new_line()
                ad.press_to_continue()


if __name__ == "__main__":
    main()