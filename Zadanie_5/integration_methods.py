import numpy as np


def gauss_legendre(num_nodes, a, b):
    nodes, weights = np.polynomial.legendre.leggauss(num_nodes)
    nodes = 0.5 * (b - a) * nodes + 0.5 * (a + b)
    weights = 0.5 * (b - a) * weights
    return nodes, weights


def gauss_chebyshev(num_nodes, a, b):
    nodes = np.cos((2 * np.arange(1, num_nodes + 1) - 1) * np.pi / (2 * num_nodes))
    nodes = 0.5 * (b - a) * nodes + 0.5 * (a + b)
    weights = np.pi / num_nodes * np.ones(num_nodes)
    return nodes, weights
