import numpy as np


# Wczytywanie macierzy z pliku
def read_matrix_from_file(file):
    with open(file, encoding="utf-8") as plik:
        linie = plik.readlines()
    a_array = []
    b_array = []
    for linia in linie:
        linia = linia.strip().replace('−', '-')
        dane = linia.strip().split(';')
        dane_a = [float(x) for x in dane[:-1]]
        dane_b = float(dane[-1])
        b_array.append(dane_b)
        a_array.append(dane_a)  # Macierz A
    d_array = np.diag(np.diag(a_array))  # Macierz D - diagonalna
    l_array = np.tril(a_array, -1)  # Macierz L - poddiagonalna
    u_array = np.triu(a_array, 1)  # Macierz U - naddiagonalna
    return a_array, b_array, d_array, l_array, u_array


def is_matrix_convergent(file):
    matrix = read_matrix_from_file(file)[0]
    diag = np.diag(np.diag(matrix))
    lower = np.tril(matrix, -1)
    upper = np.triu(matrix, 1)
    iterative_matrix = np.linalg.inv(diag).dot(lower + upper)

    spectral_radius = max(abs(np.linalg.eigvals(iterative_matrix)))

    if spectral_radius < 1:
        return True
    else:
        return False


def jacobi_method(matrix, case, case_value):
    file = read_matrix_from_file(matrix)
    A = file[0]
    B = file[1]
    D = file[2]
    L = file[3]
    U = file[4]
    N = np.linalg.inv(D)
    n = len(A)
    X = [0.0] * n
    if case == 1:
        while True:
            x_i = -N.dot((L + U).dot(X)) + N.dot(B)
            if np.linalg.norm(x_i - X) < case_value:
                break
            X = x_i
    elif case == 2:
        for i in range(int(case_value)):
            x_i = -N.dot((L + U).dot(X)) + N.dot(B)
            X = x_i
    return X
