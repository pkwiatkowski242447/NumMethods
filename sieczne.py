import funkcje as fun


def sieczne(x1, x2, f, zatrzymanie, wartosc):
    liczba_iteracji = 0
    f_x1 = fun.y(x1, f)
    f_x2 = fun.y(x2, f)
    if f_x1 * f_x2 > 0:
        print("Funkcja nie ma różnych znaków na krańcach przedziału")
    else:
        if zatrzymanie == "a":
            while abs(x2 - x1) > wartosc:
                liczba_iteracji += 1
                x_i = x2 - ((f_x2 * (x2 - x1)) / (f_x2 - f_x1))
                f_xi = fun.y(x_i, f)
                x1 = x2
                f_x1 = f_x2
                x2 = x_i
                f_x2 = f_xi
            print(f"Wynik osiągniety metodą siecznych: {x_i} po {liczba_iteracji} liczbie iteracji")
        if zatrzymanie == "b":
            while wartosc > 0:
                wartosc -= 1
                x_i = x2 - ((f_x2 * (x2 - x1)) / (f_x2 - f_x1))
                f_xi = fun.y(x_i, f)
                x1 = x2
                f_x1 = f_x2
                x2 = x_i
                f_x2 = f_xi
            print(f"Wynik osiągniety metodą siecznych: {x_i}")
