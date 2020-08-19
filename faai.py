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


def plot_vector(v, color=None):
    
    v1 = v[0]
    v2 = v[1]
    
    c = 'black' if color is None else color
    
    plt.arrow(0, 0, v1, v2, head_width=.2, head_length=.4, length_includes_head=True, color=c)