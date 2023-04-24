from numpy import double
import calc
import plots

"""
    Funkcja wczytująca plik z węzłami interpolacyjnymi. 
    interpolation_nodes -> tablica z wczytanymi węzłami interpolacyjnymi, konwertując te wartości na double
    W obrębie tej funkcji występuje też sprawdzanie czy węzły interpolacyjne znajdują się w podanym przez użytkownika
    zakresie
"""


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


"""
    Funkcja menu_start: 
        1.Wyświetlenie wszystkich wbudowanych funkcji 
        2.Wybór przez użytkownika funkcji 
        3.Po wybraniu funkcji, użytkownik wybiera przedział interpolacji 
        4.Sprawdzenie czy przedział jest poprawny (czy lewy kraniec przedziału nie jest większy niż prawy oraz 
        czy prawy nie jest mniejszy niż lewy)
        5.Użytkownik podaje nazwę pliku z którego będą wczytywane węzły interpolacyjne
        6.Jeżeli wczytane węzły nie spełniają wymagań to program kończy swoje działanie
        7.Podanie argumentu przez użytkownika dla którego będzie liczona wartość interpolacji 
        8.Sprawdzenie czy dany argument znajduje się w przedziale interpolacji 
        9.Następnie zostaje liczona wartość funkcji dla węzłów interpolacyjnych przez funkcję interp_nodes_values
        10.Na koniec zostaje zostaje zwrócona przybliżona wartość w punkcie podanym przez użytkownika za pomocą 
        interpolacji Newtona dla nierównych odstępu argumentu 
"""


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
            if x1 >= x2:
                print("Lewy kraniec przedziału musi być mniejszy niż prawy koniec przedziału")
                break
            file_name = input("Podaj nazwę pliku z którego będą wczytywane węzły intepolacyjne: ")
            is_valid = read_from_file(file_name, x1, x2)[0]
            if is_valid is False:
                print("Wczytane węzły nie spełniają wymagań")
                break
            interp_nodes = read_from_file(file_name, x1, x2)[1]
            x = double(input("Podaj wartość dla której będzie liczona interpolacja: "))
            if x < x1 or x > x2:
                print("Wartosc ta nie znajduje się w przedziale")
                break
            else:
                interp_nodes_values = calc.y_values_interp_nodes(interp_nodes, function_choice)
                print(calc.newton_interpolation(x, interp_nodes, interp_nodes_values))
                plots.function_plot(x1, x2, function_choice, interp_nodes, x)
        elif function_choice == 11:
            break
        else:
            print("Blad wyboru")
