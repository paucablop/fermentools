import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_pls_fermentation(prediction: np.ndarray, fermentation_hplc: pd.DataFrame) -> None:
    """
    Plots the predicted concentration and the reference hplc measurements.
    @param prediction load the predictions.
    @param fermentation_hplc load the reference hplc measurements.
    """

    time = np.linspace(0, len(prediction), len(prediction))

    plt.figure(figsize=(10, 3))
    plt.title("Fermentation frofile")
    plt.xlabel("Time (h)")
    plt.ylabel("Glucose concentration (g/l)")
    plt.plot(time * 1.28 / 60, prediction, color="blue")
    plt.plot(fermentation_hplc["time"], fermentation_hplc["glucose"], "o", color="red")
    return None

def plot_pls_training(predictions: np.ndarray, reference: np.ndarray) -> None:
    """
    Plots the PLS predictions and the reference hplc measurements for the training set.
    @param predictions predicted concentrations.
    @param reference reference hplc measurements.
    """

    plt.figure(figsize=(5, 4))
    plt.title("Predictions")
    plt.xlabel("Reference")
    plt.ylabel("Prediction")
    plt.plot(reference, predictions, "o", color="blue")
    plt.plot(
        [predictions.min().min(), predictions.max().max()],
        [predictions.min().min(), predictions.max().max()],
        color="red",
    )

    return None

def plot_spectra(spectra: pd.DataFrame, title: str, xlabel: str, ylabel: str):
    """
    Plots spectra.
    @param spectra dataframe containing the spectra with the wavenumbers as columns.
    @param title title of plot
    @param xlabel x-axis label
    @param ylabel y-axis label
    """

    plt.figure(figsize=(10, 3))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(spectra.columns, spectra.T.values)
    return None
