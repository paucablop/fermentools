import matplotlib.pyplot as plt
import numpy as np


def plot_mechanistic_fermentation(time: np.ndarray, concentrations: np.ndarray) -> None:
    """
    Plots the predicted concentration and the reference hplc measurements.
    @param prediction load the predictions.
    @param fermentation_hplc load the reference hplc measurements.
    """
    plt.figure(figsize=(10, 3))
    plt.plot(time, concentrations[:,0], color="blue", label="Glucose [g/L]")
    plt.plot(time, concentrations[:,1], color="red", label="Biomass [g/L]")
    plt.plot(time, concentrations[:,2], color="black", label="Ethanol [g/L]")
    plt.legend()
    plt.title("Fermentation profile")
    plt.ylabel("Concentration")
    plt.xlabel("Time [h]")
