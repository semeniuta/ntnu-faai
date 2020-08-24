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


def plot_vector(v, origin=None, color=None):
    
    v1 = v[0]
    v2 = v[1]

    if origin is None:
        origin = (0, 0)
    
    c = 'black' if color is None else color
    
    plt.arrow(origin[0], origin[1], v1, v2, 
              head_width=.2, head_length=.4, length_includes_head=True, color=c)


def rotation_matrix_2d(theta):

    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([[c, -s], [s, c]])


def generate_noisy_data_poly1d(coefs, normal_std=1., xmin=-5, xmax=5, step=0.5):

    x = np.arange(xmin, xmax, step)

    y_true = np.zeros_like(x)
    for i, c in enumerate(coefs):
        y_true += c*(x**i)

    noise = np.random.normal(scale=normal_std, size=len(y_true))
    y_noisy = y_true + noise

    return x, y_noisy


def generate_noisy_data_poly1d_Ab(coefs, normal_std=1., xmin=-5, xmax=5, step=0.5):

    x = np.arange(xmin, xmax, step)

    y_true = np.zeros_like(x)
    for i, c in enumerate(coefs):
        y_true += c*(x**i)

    noise = np.random.normal(scale=normal_std, size=len(y_true))
    y_noisy = y_true + noise

    A_size = (len(x), len(coefs))
    A = np.ones(A_size)
    for j in range(1, len(coefs)):
        A[:, j] = x**j

    return A, y_noisy
