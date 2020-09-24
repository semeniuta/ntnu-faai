import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import multivariate_normal


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


class NoisyPolynomial:

    def __init__(self, coefs, normal_std=1., xmin=-5, xmax=5, step=0.5, random_state=None):

        def compute_y_true(x, coefs):
            
            y_true = np.zeros_like(x)
            for i, c in enumerate(coefs):
                y_true += c*(x**i)
            
            return y_true

        def create_A(x, coefs):
            
            A_size = (len(x), len(coefs))
            A = np.ones(A_size)
            for j in range(1, len(coefs)):
                A[:, j] = x**j

            return A

        self.x = np.arange(xmin, xmax, step)
        self.y_true = compute_y_true(self.x, coefs)
        
        if random_state is not None:
            np.random.seed(random_state)
        noise = np.random.normal(scale=normal_std, size=len(self.y_true))
        
        self.y_noisy = self.y_true + noise

        self.A = create_A(self.x, coefs)
    
    @property
    def b(self):
        return self.y_noisy


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


def generate_mvnormal_clusters(mus, covs, sizes, seed=None):

    if seed is not None:
        np.random.seed(seed)

    n_points = sum(sizes)
    xs = np.zeros(n_points)
    ys = np.zeros(n_points)
    labels = np.zeros(n_points, dtype=int)

    start_from = 0
    lb = 0
    for mu, cov, sz in zip(mus, covs, sizes):

        x, y = np.random.multivariate_normal(mu, cov, sz).T

        next_start_from = start_from + sz

        xs[start_from:next_start_from] = x
        ys[start_from:next_start_from] = y
        labels[start_from:next_start_from] = lb

        start_from = next_start_from
        lb += 1

    return xs, ys, labels


def mvnormal_distrib_map(mu, cov, observations, padding_factor=0.2, grid_prec=0.25):
    """
    Create a discritized map of a multivariate normal distribution on domain
    defined by the observations

    :param mu: Mean of a multivariate normal ((m x 1) array)
    :param cov: Covariance matrix of a multivariate normal ((n x n array))
    :param observations: An (m x n) NumPy array or Pandas data frame,
                         where n is the dimension of the data
                         and m is the number of observations
    :param padding_factor: a factor by which the data span domain is extended
    :param grid_prec: precision of discretization (distance between two consecutive
                      grid points)
    :return:
    """

    dim = observations.shape[1]

    obs_min = np.min(observations, axis=0)
    obs_max = np.max(observations, axis=0)

    dataspan = obs_max - obs_min
    padding = dataspan * padding_factor
    domain = np.array([obs_min - padding, obs_max + padding])

    aranges = [np.arange(domain[0, j], domain[1, j], grid_prec)
               for j in range(dim)]
    grid_x, grid_y = np.meshgrid(*aranges)

    def make_mv_normal(mu, cov):
        def fn(grid_x, grid_y):

            distrib = np.zeros(grid_x.shape)

            for i in range(grid_x.shape[0]):
                for j in range(grid_x.shape[1]):
                    x = np.array([grid_x[i, j], grid_y[i, j]])
                    distrib[i, j] = multivariate_normal.pdf(x, mu, cov)

            return distrib

        return fn

    mv_normal = make_mv_normal(mu, cov)

    distrib_map = mv_normal(grid_x, grid_y)

    return grid_x, grid_y, distrib_map


def get_axis_extent(grid_x, grid_y):
    """
    Get a tuple of (left, right, bottom, top)
    from the meshgrid output. Used for the extent
    parameter in matplotlib
    """

    left = grid_x[0, 0]
    right = grid_x[0, -1]

    bottom = grid_y[-1, 0]
    top = grid_y[0, 0]

    return left, right, bottom, top


def plot_frozen_distrib(x0, x1, distrib, linspace_num=200, fill_alpha=0.4, **plot_kvargs):
    """
    Visualize 1D continuous distribution on the given domain range
    """

    x = np.linspace(x0, x1, num=linspace_num)
    y = distrib.pdf(x)
    plt.plot(x, y, **plot_kvargs)

    fb_kvargs = {'alpha': fill_alpha}
    if 'color' in plot_kvargs:
        fb_kvargs['color'] = plot_kvargs['color']
    plt.fill_between(x, y, **fb_kvargs)
