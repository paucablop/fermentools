from fermentools.datasets.ir import load_training_data, load_fermentation_spectra_data, load_fermentation_hplc_data
from fermentools.datasets.fluorescence import load_filtered_fluorescence_data, load_unfiltered_fluorescence_data

def test_ir_train_loadings():
  """
  Test the loading of the training data.
  """
  # Arrange

  # Act
  spectra, reference = load_training_data()

  # Assert
  assert spectra.shape == (21, 1047)
  assert reference.shape == (21, 1)


def test_ir_fermentation_loadings():
  """
  Test the loading of the fermentation data.
  """
   # Arrange

  # Act
  spectra = load_fermentation_spectra_data()
  reference = load_fermentation_hplc_data()

  # Assert
  assert spectra.shape == (1629, 1047)
  assert reference.shape == (34, 6)


def test_fluorescence_loadings():
  """
  Test the loading of the fluorescence data
  """
  # Arrange

  # Act
  eem_filtered, excitation_wavenumbers, emission_wavenumbers = load_filtered_fluorescence_data()
  eem_unfiltered, _, _ = load_unfiltered_fluorescence_data()

  # Assert
  assert eem_filtered.shape == (10, 43, 91)
  assert eem_unfiltered.shape == (10, 43, 91)