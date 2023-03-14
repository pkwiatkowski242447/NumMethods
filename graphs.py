import matplotlib.pyplot as plt
import functions as f
import numpy as np


def inital_graph(fun, x1, x2):
    y_values = []
    x_values = np.array([x1, x2])
    for i in range(len(x_values)):
        y_values.append(f.y(x_values[i], fun))
    plt.plot(x_values, y_values)
    plt.title("Wykres wybranej funkcji")
    plt.xlabel("Wartości na osi X")
    plt.ylabel("Wartości na osi Y")
    plt.show()


def final_graph(fun, x1, x2, bis, siecz):
    y_values = []
    x_values = np.array([x1, x2])
    for i in range(len(x_values)):
        y_values.append(f.y(x_values[i], fun))
    plt.plot(x_values, y_values)
    plt.title("Wykres wybranej funkcji")
    plt.xlabel("Wartości na osi X")
    plt.ylabel("Wartości na osi Y")
    plt.plot(bis, f.y(bis, fun), marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
    plt.plot(siecz, f.y(siecz, fun), marker="x", markersize=10, markeredgecolor="red", markerfacecolor="blue")
    plt.show()
