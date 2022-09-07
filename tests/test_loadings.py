from dtuprosys.datasets import load_training_data, load_fermentation_spectra_data, load_fermentation_hplc_data

def test_train_loadings():
  """
  Test the loading of the training data.
  """
  # Arrange

  # Act
  spectra, reference = load_training_data()

  # Assert
  assert spectra.shape == (21, 1047)
  assert reference.shape == (21, 1)


def test_fermentation_loadings():
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
