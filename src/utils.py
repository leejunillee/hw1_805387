import matplotlib.pyplot as plt
import numpy as np
import math as math


def plot_iterations_objective(path_to):
    x = range(len(path_to))
    y = list(map( get_val , path_to))
    plt.plot(x, y, 'ro', ms=2)
    plt.xlabel('iteration #')
    plt.ylabel('object f(x)')
    plt.show()
