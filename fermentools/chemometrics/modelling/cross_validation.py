from mbpls.mbpls import MBPLS
from sklearn.model_selection import validation_curve, LeaveOneOut
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt
import pandas as pd


def cross_validation(X: pd.DataFrame, y: pd.DataFrame) -> None:
    """
    Performs cross-validation on the data. By default it performs a leave-one-out cross-validation.
    @param X spectra dataframe containing the spectra with the wavenumbers as columns.
    @param y dataframe containing the reference hplc measurements.
    """

    # Initialize model
    model = MBPLS()

    # Initialize cross-validation parameters
    cv = LeaveOneOut()
    param_name = "n_components"
    param_range = range(1, 8)
    scoring = "neg_root_mean_squared_error"

    # Perform cross-validation
    test_scores, validation_scores = validation_curve(
        model,
        X.values,
        y.values,
        cv=cv,
        param_name=param_name,
        param_range=param_range,
        scoring=scoring,
    )

    # Plot results
    plt.figure(figsize=(10, 3))
    plt.title("Cross-validation")
    plt.xlabel(param_name)
    plt.ylabel("root mean squared error")
    plt.plot(
        param_range, -test_scores.mean(axis=1), "o-", label="Test error", color="red"
    )
    plt.plot(
        param_range,
        -validation_scores.mean(axis=1),
        "o-",
        label="Validation error",
        color="blue",
    )
    plt.legend()
    plt.show()

    return None
