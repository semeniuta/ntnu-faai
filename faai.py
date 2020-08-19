import numpy as np
from matplotlib import pyplot as plt


def canvas(xlim, ylim):

    plt.axis('equal')
    plt.gca().set_adjustable('box')

    plt.grid(color='gray', linestyle='--', linewidth=1, alpha=0.5)

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.xlim(xlim)
    plt.ylim(ylim)

    plt.xticks(np.arange(xlim[0], xlim[1]+1))
    plt.yticks(np.arange(ylim[0], ylim[1]+1))
