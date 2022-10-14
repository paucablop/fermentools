import numpy as np
import os

PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def load_filtered_fluorescence_data():
    """
    returns the emission - excitation matrix for the filtered data
    @return fluorescence_spectra: tensor with the filtered data (sample x excitation x emission)
    @return emission_wavelengths: array with the emission wavelengths
    @return excitation_wavelengths: array with the excitation wavelengths
    """

    fluorescence_spectra = np.genfromtxt(PACKAGE_DIRECTORY + "/data/excitation_emission_matrix.csv", delimiter=",")
    emission_wavenumbers = np.genfromtxt(PACKAGE_DIRECTORY + "/data/emission_wavenumbers.csv", delimiter=",")
    excitation_wavenumbers = np.genfromtxt(PACKAGE_DIRECTORY + "/data/excitation_wavenumbers.csv", delimiter=",")

    fluorescence_spectra = fluorescence_spectra.reshape(20, 43, 91)

    return fluorescence_spectra[0:10,:,:], emission_wavenumbers, excitation_wavenumbers


def load_unfiltered_fluorescence_data():
    """
    returns the emission - excitation matrix for the filtered data
    @return fluorescence_spectra: tensor with the unfiltered data (sample x excitation x emission)
    @return emission_wavelengths: array with the emission wavelengths
    @return excitation_wavelengths: array with the excitation wavelengths
    """
    
    fluorescence_spectra = np.genfromtxt(PACKAGE_DIRECTORY + "/data/excitation_emission_matrix.csv", delimiter=",")
    emission_wavenumbers = np.genfromtxt(PACKAGE_DIRECTORY + "/data/emission_wavenumbers.csv", delimiter=",")
    excitation_wavenumbers = np.genfromtxt(PACKAGE_DIRECTORY + "/data/excitation_wavenumbers.csv", delimiter=",")

    fluorescence_spectra = fluorescence_spectra.reshape(20, 43, 91)

    return fluorescence_spectra[10:20,:,:], emission_wavenumbers, excitation_wavenumbers