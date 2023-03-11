import funkcje as fun


def bisekcja(x1, x2, f, zatrzymanie, wartosc):
    liczba_iteracji = 0
    f_x1 = fun.y(x1, f)
    f_x2 = fun.y(x2, f)
    if f_x1 * f_x2 > 0:
        print("Funkcja nie ma różnych znaków na krańcach przedziału")
    if zatrzymanie == "a":
        while abs(x2 - x1) > wartosc:
            liczba_iteracji += 1
            x = (x1 + x2) / 2
            f_srodek = fun.y(x, f)
            if f_x2 * f_srodek < 0:
                x1 = x
            else:
                x2 = x
                f_x2 = f_srodek
        print(f"Wynik osiągniety metodą bisekcji: {x} po {liczba_iteracji} liczbie iteracji")
    if zatrzymanie == "b":
        while wartosc > 0:
            wartosc -= 1
            x = (x1 + x2) / 2
            f_srodek = fun.y(x, f)
            if f_x2 * f_srodek < 0:
                x1 = x
            else:
                x2 = x
                f_x2 = f_srodek
        print(f"Wynik osiągniety metodą bisekcji: {x}")
