import pandas as pd
import addon as ad
import menu as mn
import calc as cl


def main():
    program_option = 0
    while program_option != 2:
        ad.clear_screen()
        mn.general_menu()
        program_option = int(input("Twój wybór: "))
        if program_option == 1:
            ad.new_line()
            number_of_equations = int(input("Podaj liczbę równań w układzie równań: "))
            ad.clear_screen()
            mn.print_coefficient_entry()
            user_choice = int(input("Twój wybór: "))
            double_dimension = pd.DataFrame()
            if user_choice == 1:
                ad.new_line()
                for equation_number in range(number_of_equations):
                    coefficients_list = []
                    for index in range(number_of_equations):
                        coefficients_list.append(float(input(
                            "Podaj wartość współczynnika przy x" + str(index + 1) + " w " + str(
                                equation_number + 1) + ". równaniu układu: ")))
                    coefficients_list.append(float(input("Podaj wynik równania: ")))
                    coefficients_list = pd.Series(coefficients_list)
                    double_dimension = pd.concat([double_dimension, coefficients_list.to_frame().T], ignore_index=True)
                ad.new_line()
                mn.print_criterion_choice()
                crit = int(input("Twój wybór: "))
                if crit == 1:
                    value = float(input("\nPodaj wartość dokładności: "))
                else:
                    value = int(input("\nW ilu iteracjach algorytm ma wyznaczyć miejsce zerowe: "))
                cl.iterative_solving(double_dimension.iloc[:, :number_of_equations],
                                     double_dimension.iloc[:, number_of_equations:(number_of_equations + 1)],
                                     crit, value)
                ad.new_line()
                ad.press_to_continue()
            elif user_choice == 2:
                ad.new_line()
                file_name = input("Podaj nazwę pliku, z którego mają zostać odczytane współczynniki: ")
                double_dimension = ad.read_coefficients_from_files(file_name, number_of_equations)
                ad.new_line()
                mn.print_criterion_choice()
                crit = int(input("Twój wybór: "))
                if crit == 1:
                    value = float(input("\nPodaj wartość dokładności: "))
                else:
                    value = int(input("\nW ilu iteracjach algorytm ma wyznaczyć miejsce zerowe: "))
                cl.iterative_solving(double_dimension.iloc[:, :number_of_equations],
                                     double_dimension.iloc[:,
                                     number_of_equations:(number_of_equations + 1)],
                                     crit, value)
                ad.new_line()
                ad.press_to_continue()
            else:
                print("Wybrano opcję, która nie znajduje się w menu.")
                ad.press_to_continue()
        elif program_option == 2:
            print("\nWybrano zakończenie programu.")
            ad.press_to_continue()


if __name__ == "__main__":
    main()
