import addon as ad

def horner_scheme(arg, array, num):
    itr = 0
    temp = array[itr]
    while itr < num - 1:
        temp = temp * arg + array[itr + 1]
        itr += 1
    return temp


def calculate(function_number, start, end, cond, value):                            # function_num oznacza numer wybranej przez użytkownika funkcji
    print("Funkcja przeznaczona do obliczania miejsc zerowych zadanej funkcji.")    # start to początek przedziału, na którym szukane będzie miejsce zerowe
    input("Naciśnij klawisz, aby kontynuować...")                                   # end oznacza koniec tego przedziału
    ad.clear()                                                                      # cond oznacza wybrany przez użytkownika warunek stopu
                                                                                    # value to wartość dotycząca warunku stopu, a więc liczba iteracji lub też zadana dokładność


def bisection():
    return 0


def secant_method():
    return 0
