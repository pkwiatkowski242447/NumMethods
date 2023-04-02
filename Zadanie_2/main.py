import jacobi_method as jc
import numpy as np


def menu():
    while True:
        plik = str(input("Wybierz plik od a.txt do j.txt: "))
        if jc.is_matrix_convergent(plik) == False:
            print("Podana macierz nie jest zbiezna")
        else:
            print("Wybierz warunek końca")
            print("1.Warunek dokładności")
            print("2.Liczba iteracji")
            wybor_zatrzymania = int(input("Wybierz: "))
            if wybor_zatrzymania == 1:
                wartosc = np.double(input("Podaj dokladnosc: "))
                print(jc.jacobi_method(plik, wybor_zatrzymania, wartosc))
            if wybor_zatrzymania == 2:
                wartosc = np.double(input("Podaj liczbe iteracji: "))
                print(jc.jacobi_method(plik, wybor_zatrzymania, wartosc))
            else:
                break


if __name__ == '__main__':
    menu()
