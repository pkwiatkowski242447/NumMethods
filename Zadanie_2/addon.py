import os
import pandas as pd


def clear_screen():
    if os.name == 'posix':
        os.system('clear')  # Czyszczenie konsoli dla systemów Linux / Mac
    else:
        os.system('cls')  # Czyszczenie konsoli dla systemu Windows


def press_to_continue():
    input("Naciśnij dowolny klawisz, aby kontynuować...")


def new_line():
    print('')


def read_coefficients_from_files(file_name, degree):
    double_dimension = pd.DataFrame()
    file = open(file_name, "r")
    for line in file:
        list_of_numbers = []
        line.replace('\n', '')
        list_of_chars = line.split(';')
        for number in list_of_chars:
            list_of_numbers.append(float(number))
        series_of_numbers = pd.Series(list_of_numbers, dtype=float)
        double_dimension = pd.concat([double_dimension, series_of_numbers.to_frame().T], ignore_index=True)
    return double_dimension
