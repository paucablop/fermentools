import numpy as np


class ExtendedKalmanFilter:
    def __init__(
        self,
        measurement_covariance: np.ndarray,
        model_covariance: np.ndarray,
    ):
        self.measurement_convariance = measurement_covariance
        self.model_covariance = model_covariance

    def calculate(measurements):
        # Step 1. Get the initial values
        current_state: np.ndarray
        current_uncertainty: np.ndarray
        priori_state_prediction: np.ndarray
        priori_uncertainty_prediction: np.ndarray
        measurements: np.ndarray
        posteriori_state_prediction: np.ndarray
        posteriory_uncertainty_prediction: np.ndarray

