import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def create_normal_curve(values, mean, std_dev):
    x = np.linspace(values.min(), values.max(), 1000)
    return stats.norm.pdf(x, loc=mean, scale=std_dev)


def create_data(*args, **kwargs):
    return np.random.normal(*args, **kwargs)


def multiple_bins_graph(values, bin_counts, visuals_histograms, horizontal, normal_curve=None):

    plots = (len(bin_counts), 1)
    if horizontal:
        plots = plots[::-1]
    figsize = [i * figsize_factor for i in plots[::-1]]

    fig, axes = plt.subplots(*plots, figsize=figsize)
    if not isinstance(axes, np.ndarray):
        axes = np.array([axes])
    for ax, bins in zip(axes, bin_counts):
        ax.hist(values, bins=bins, **visuals_histograms)
        ax.set_title(f'{bins} Bins')
        if normal_curve:
            x = np.linspace(values.min(), values.max(), 1000)
            nc = stats.norm.pdf(x, loc=normal_curve['mean'], scale=normal_curve['std_dev'])
            ax.plot(x, nc, **normal_curve['visuals_normal_dist'])

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    mean = 12
    std_dev = 1
    size = 30000
    bin_counts = [5, 15, 25]
    horizontal = True
    figsize_factor = 5
    visuals_histograms = {
        'edgecolor': 'black',
        'density': True,
    }
    visuals_histograms_2 = {
        'edgecolor': 'black',
    }
    visuals_normal_dist = {
        'color': 'red',
        'linewidth': 2,
    }

    values = create_data(loc=mean, scale=std_dev, size=size)

    multiple_bins_graph(values, bin_counts, visuals_histograms_2, horizontal)
    multiple_bins_graph(values, bin_counts[-1:], visuals_histograms, horizontal, normal_curve={'mean':mean, 'std_dev':std_dev, 'visuals_normal_dist': visuals_normal_dist})
