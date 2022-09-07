import pandas as pd
import os

PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def load_training_data():
    """
    Loads the training data.
    @return train_spectra: spectra in the training data.
    @return train_hplc: hplc in the training data.
    """
    train_spectra = pd.read_csv(PACKAGE_DIRECTORY + "/data/train_spectra.csv")
    train_spectra.columns = train_spectra.columns.astype(float)
    train_hplc = pd.read_csv(PACKAGE_DIRECTORY + "/data/train_hplc.csv")

    return train_spectra, train_hplc


def load_fermentation_spectra_data():
    """
    Loads the fermentation data.
    @return fermentation_spectra: spectra measured during the fermentation.
    """
    fermentation_spectra = pd.read_csv(
            PACKAGE_DIRECTORY + "/data/fermentation_spectra.csv"
    )
    fermentation_spectra.columns = fermentation_spectra.columns.astype(float)

    return fermentation_spectra


def load_fermentation_hplc_data():
    """
    Loads the fermentation data.
    @return fermentation_hplc: hplc measured during the fermentation.
    """
    fermentation_hplc = pd.read_csv(PACKAGE_DIRECTORY + "/data/fermentation_hplc.csv")

    return fermentation_hplc