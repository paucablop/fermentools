from typing import Any, Tuple, Literal, Optional, Union
from sklearn.base import BaseEstimator
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression
from sklearn.pipeline import Pipeline
from sklearn.utils.validation import check_is_fitted
from sklearn.exceptions import NotFittedError


def extract_and_validate_model(
    model: Union[BaseEstimator, Pipeline],
    model_type: Literal["pca", "pls"],
) -> Tuple[Optional[Pipeline], Union[PCA, PLSRegression]]:
    """
    Validate and extract a PCA or PLS model, optionally from a pipeline.

    This function checks whether the provided model or the final step
    in a pipeline is of the expected type (`PCA` or `PLSRegression`) and whether
    it has been fitted. It also separates any preceding pipeline steps (transformers)
    from the estimator.

    Parameters
    ----------
    model : BaseEstimator or Pipeline
        A fitted scikit-learn estimator or a Pipeline containing a PCA or PLSRegression
        model as the final step.

    model_type : {'pca', 'pls'}
        The expected type of model. Must be one of 'pca' or 'pls'.

    Returns
    -------
    transformer : Pipeline or None
        A pipeline containing all steps before the final estimator if the input
        is a Pipeline. `None` if the input is not a pipeline.

    estimator : PCA or PLSRegression
        The validated and fitted PCA or PLSRegression estimator.

    Raises
    ------
    ValueError
        If `model_type` is not 'pca' or 'pls'.

    TypeError
        If the final model is not of the expected type.

    NotFittedError
        If the estimator has not been fitted yet.
    """

    # Extract the model
    if isinstance(model, Pipeline):
        transformer = model[:-1]
        estimator = model[-1]
    else:
        transformer = None
        estimator = model

    # Validate the model type
    if model_type.lower() == "pca":
        expected_type = PCA
    elif model_type.lower() == "pls":
        expected_type = PLSRegression
    else:
        raise ValueError("model_type must be either 'pca' or 'pls'")

    if not isinstance(estimator, expected_type):
        raise TypeError(f"Expected a {expected_type.__name__}, got {type(estimator)}")

    try:
        check_is_fitted(
            estimator,
        )
    except NotFittedError as e:
        raise NotFittedError(
            f"The provided {model_type.upper()} model is not fitted."
        ) from e

    return transformer, estimator


def get_cut_wavenumbers_from_pipeline(pipeline: Pipeline) -> Optional[Any]:
    """
    Retrieve the `cut_wavenumbers` attribute from a 'rangecut' step in a Pipeline, if present.

    Parameters
    ----------
    pipeline : Pipeline
        A scikit-learn Pipeline object.

    Returns
    -------
    cut_wavenumbers : Any or None
        The `cut_wavenumbers` attribute from the 'rangecut' step, or None if the step is absent.
    """
    if not isinstance(pipeline, Pipeline):
        raise TypeError("Expected a scikit-learn Pipeline object.")

    if "rangecut" in pipeline.named_steps:
        rangecut_step = pipeline.named_steps["rangecut"]
        if hasattr(rangecut_step, "wavenumbers_"):
            return rangecut_step.wavenumbers_

    return None
