from scipy.signal import savgol_filter

import pandas as pd


class RangeCut:
    """
    Cuts a dataframe selecting the wavenumbers between start and end.
    """

    def __init__(self, start: int, end: int):
        """
        Constructor.
        @param start start wavenumber
        @param end end wavenumber
        """
        self.start = start
        self.end = end

    def apply_to(self, x: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the cut to the dataframe.
        @param x dataframe containing the spectra with the wavenumbers as columns.
        @return range cut dataframe
        """
        return x.loc[:, self.start : self.end]


class Derivative:
    """
    Calculates the derivative of a each row in a dataframe using the Savitzky-Golay filter.
    """

    def __init__(
        self, derivative_order: int, window_length: int = 15, polynomial_order: int = 1
    ):
        """
        Constructor.
        @param derivative_order derivative order
        @param window_length window length
        @param polynomial_order polynomial order
        """
        self.derivative_order = derivative_order
        self.window_length = window_length
        self.polynomial_order = polynomial_order

    def apply_to(self, x: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the derivative to the dataframe.
        @param x dataframe containing the spectra with the wavenumbers as columns.
        @return dataframe with derivative
        """
        derivate = pd.DataFrame(savgol_filter(
            x, self.window_length, self.polynomial_order, deriv=self.derivative_order
        ))
        derivate.columns = x.columns
        return derivate
