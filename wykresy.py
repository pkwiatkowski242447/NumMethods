import matplotlib.pyplot as plt
import funkcje as f
import numpy as np


def wykres(fun, x1, x2):
    wartosci_y = []
    wartosci_x = np.array([x1, x2])
    for i in range(len(wartosci_x)):
        wartosci_y.append(f.y(i, fun))
    plt.plot(wartosci_x, wartosci_y)
    plt.title("Wykres wybranej funkcji")
    plt.xlabel("Wartości na osi X")
    plt.ylabel("Wartości na osi Y")
    plt.show()
