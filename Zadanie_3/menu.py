import os
from numpy import double


def read_from_file(filename, x_1, x_2):
    result = True
    interpolation_nodes = []
    with open(filename, 'r') as file:
        for line in file:
            interpolation_nodes.append(double(line.strip()))
    for tab_element in interpolation_nodes:
        if tab_element < x_1 or tab_element > x_2:
            result = False
    return result, interpolation_nodes


def menu_start():
    while True:
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
        print("11. Koniec działania programu")
        function_choice = int(input("Wybierz funkcję: "))
        if 0 < function_choice < 11:
            x1 = double(
                input("Podaj lewy kraniec przedziału interpolacji: "))
            x2 = double(
                input("Podaj prawy kraniec przedziału interpolacji: "))
            file_name = input("Podaj nazwę pliku z którego będą wczytywane węzły intepolacyjne: ")
            valid = read_from_file(file_name, x1, x2)[0]
            interp_nodes = read_from_file(file_name, x1, x2)[1]
            if (valid == False):
                print("Wczytane węzły nie spełniają wymagań")
                break
            if x1 >= x2:
                print("Lewy kraniec przedziału musi być mniejszy niż prawy koniec przedziału")
            elif function_choice == 11:
                break
            else:
                print("Blad wyboru")
