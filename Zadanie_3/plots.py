import calc
import numpy as np
import matplotlib.pyplot as plt


def function_plot(x1, x2, function_choice, interpolation_nodes):
    x_basic_function = np.linspace(x1, x2, int(x2 - x1) * 100)
    y_basic_function = calc.y_values(x_basic_function, function_choice)
    y_1 = calc.y_values(interpolation_nodes, function_choice)
    inter_val_basic = []
    inter_val = []
    for i in range(0, len(x_basic_function), 1):
        inter_val_basic[i] = calc.newton_interpolation(x_basic_function[i], interpolation_nodes, y_1)
    for i in range(0, np.size(interpolation_nodes), 1):
        inter_val[i] = calc.newton_interpolation(interpolation_nodes[i], interpolation_nodes, y_1)
    print(interpolation_nodes)
    print(inter_val)
    plt.plot(x_basic_function, y_basic_function, color="red", linewidth="2")
    plt.plot(x_basic_function, inter_val_basic, color="blue")
    plt.scatter(interpolation_nodes, inter_val, color="green", marker="o")
    plt.xlabel('oś X')
    plt.ylabel('oś Y')
    plt.title('Wykres wybranej funkcji')
    plt.legend(["Funkcja oryginalna", "Wielomian interpolujący", "węzły interpolacji"])
    plt.show()
