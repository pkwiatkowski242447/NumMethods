import pandas as pd
import numpy as np


def read_from_file(filename):
    input = np.loadtxt(filename, dtype="i", delimiter=',')
    print(input)


if __name__ == '__main__':
    read_from_file("a.txt")
