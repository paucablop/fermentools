from typing import Optional
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from numpy.typing import ArrayLike
import numpy as np


def plot_spectra(
    x: ArrayLike,
    y: ArrayLike,
    color_by: Optional[ArrayLike] = None,
    title: str = "Spectra",
    x_label: str = "Wavenumber",
    y_label: str = "Intensity",
):
    """
    Plot spectra with optional color coding based on a scalar array.

    Parameters
    ----------
    x : ArrayLike
        The x-axis data (e.g., wavenumbers), shape (n_features,)
    y : ArrayLike
        The y-axis data (e.g., intensity values), shape (n_samples, n_features)
    color_by : Optional[ArrayLike], optional
        Optional array of shape (n_samples,) for color coding the lines.
    title : str, optional
        Title of the plot (default is "Spectra").
    x_label : str, optional
        Label for the x-axis (default is "Wavenumber").
    y_label : str, optional
        Label for the y-axis (default is "Intensity").

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object.
    ax : matplotlib.axes._axes.Axes
        The axes object.
    """
    y = np.asarray(y)
    x = np.asarray(x)

    if color_by is None:
        color_by = np.zeros(y.shape[0])
    else:
        color_by = np.asarray(color_by)

    norm = Normalize(vmin=color_by.min(), vmax=color_by.max())
    cmap = cm.get_cmap("viridis")

    fig, ax = plt.subplots(figsize=(10, 4))

    for i in range(y.shape[0]):
        ax.plot(x, y[i], color=cmap(norm(color_by[i])), alpha=0.7)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True)
    plt.tight_layout()
    plt.show()

    return fig, ax
