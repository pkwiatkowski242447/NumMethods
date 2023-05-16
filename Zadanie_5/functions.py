import numpy as np

def linear(x):
    return x


def absolute(x):
    return np.abs(x)


def polynomial(x):
    return x**3 - 2*x**2 + x


def trigonometric(x):
    return np.sin(x)


def composite(x):
    return np.sin(x**2) + np.cos(x)
