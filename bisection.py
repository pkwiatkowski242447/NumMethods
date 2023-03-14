import functions as fun


def bisection(x1, x2, f, zatrzymanie, value):
    iterations = 0
    f_x1 = fun.y(x1, f)
    f_x2 = fun.y(x2, f)
    if f_x1 == 0:
        return [x1, 0]
    elif f_x2 == 0:
        return [x2, 0]
    else:
        if f_x1 * f_x2 > 0:
            print("Funkcja nie ma różnych znaków na krańcach przedziału")
        else:
            if zatrzymanie == "a":
                while abs(x2 - x1) > value:
                    iterations += 1
                    x = (x1 + x2) / 2
                    f_mid = fun.y(x, f)
                    if f_x2 * f_mid < 0:
                        x1 = x
                    else:
                        x2 = x
                        f_x2 = f_mid
                return [x, iterations]
            if zatrzymanie == "b":
                while value > 0:
                    value -= 1
                    x = (x1 + x2) / 2
                    f_mid = fun.y(x, f)
                    if f_x2 * f_mid < 0:
                        x1 = x
                    else:
                        x2 = x
                        f_x2 = f_mid
                return x
