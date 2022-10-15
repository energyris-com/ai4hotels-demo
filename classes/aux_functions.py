import numpy as np


def make_one_input(series, steps):
    x = series[-1 - steps:-1, :]
    x = np.expand_dims(x, 0)
    return x