import calc
import numpy as np
import matplotlib.pyplot as plt


def function_plot(x1, x2, function_choice, interpolation_nodes, x):
    x_basic_function = np.linspace(x1, x2, int(x2 - x1) * 100)
    y_basic_function = calc.y_values_interp_nodes(x_basic_function, function_choice)
    y_interpolation_nodes = calc.y_values_interp_nodes(interpolation_nodes, function_choice)
    y_interpolation = calc.newton_interpolation(x_basic_function, interpolation_nodes, y_interpolation_nodes)
    interpolation_result = calc.newton_interpolation(x, interpolation_nodes, y_interpolation_nodes)
    inter_array_x = np.append(interpolation_nodes, x)
    inter_array_y = np.append(y_interpolation_nodes, interpolation_result)
    plt.plot(x_basic_function, y_basic_function, color="red", linewidth="2")
    plt.plot(x_basic_function, y_interpolation, color="blue")
    plt.scatter(inter_array_x, inter_array_y, color="green", marker="o")
    plt.xlabel('oś X')
    plt.ylabel('oś Y')
    plt.title('Wykres wybranej funkcji')
    plt.legend(["Funkcja oryginalna", "Wielomian interpolujący", "węzły interpolacji"])
    plt.show()
