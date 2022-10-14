from fermentools.datasets.ir import load_training_data
from fermentools.chemometrics.preprocessing import RangeCut, Derivative

import pandas as pd

def test_range_cut():
  """
  Test the range cut.
  """
  # Arrange
  start = 950
  end = 1550
  range_cut = RangeCut(start, end)
  spectra = load_training_data()[0]

  # Act
  spectra_cut = range_cut.apply_to(spectra)

  # Assert
  assert spectra_cut.shape == (21, 446)

def test_derivate():
  """
  Test the derivative.
  """
  # Arrange
  derivative_order = 1
  window_length = 15
  polynomial_order = 1
  derivative = Derivative(derivative_order, window_length, polynomial_order)
  spectra = load_training_data()[0]

  # Act
  spectra_derivative = derivative.apply_to(spectra)

  # Assert
  assert spectra_derivative.shape == spectra.shape
