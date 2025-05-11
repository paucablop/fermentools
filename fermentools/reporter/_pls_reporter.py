from typing import Optional, Union

from numpy.typing import ArrayLike
import numpy as np

from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

from chemotools.outliers import QResiduals, HotellingT2

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

from reporter.plot.plot_spectra import plot_spectra
from reporter._utils import (
    extract_and_validate_model,
    get_cut_wavenumbers_from_pipeline,
)


class PLSRegressionReport:
    def __init__(
        self,
        model: Union[Pipeline, PCA],
        X_train: ArrayLike,
        y_train: ArrayLike,
        X_test: Optional[ArrayLike] = None,
        y_test: Optional[ArrayLike] = None,
        wavenumbers: Optional[ArrayLike] = None,
    ):
        self.model = model
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.wavenumbers = wavenumbers
        self.transformer, self.estimator = extract_and_validate_model(
            model, model_type="pls"
        )
        self.cut_wavenumbers = get_cut_wavenumbers_from_pipeline(self.transformer)

    def plot_data(
        self,
        color_by: Optional[ArrayLike] = None,
        title: str = "Spectra",
        x_label: str = "Wavenumber",
        y_label: str = "Intensity",
    ):
        """
        Plot spectra with optional color coding.

        Parameters
        ----------
        color_by : Optional[ArrayLike]
            Optional array for color coding the points.
        """

        if self.wavenumbers is None:
            raise ValueError("Wavenumbers are not provided.")

        if color_by is None:
            color_by = self.y_train

        plot_spectra(
            x=self.wavenumbers,
            y=self.X_train,
            color_by=color_by,
            title=title,
            x_label=x_label,
            y_label=y_label,
        )

    def plot_preprocessed_data(
        self,
        color_by: Optional[ArrayLike] = None,
        title: str = "Spectra",
        x_label: str = "Wavenumber",
        y_label: str = "Intensity",
    ):
        """
        Plot preprocessed spectra with optional color coding.

        Parameters
        ----------
        color_by : Optional[ArrayLike]
            Optional array for color coding the points.
        """

        if self.wavenumbers is None:
            raise ValueError("Wavenumbers are not provided.")

        if self.cut_wavenumbers is not None:
            wavenumbers = self.cut_wavenumbers
        else:
            wavenumbers = self.wavenumbers

        if color_by is None:
            color_by = self.y_train

        plot_spectra(
            x=wavenumbers,
            y=self.transformer.transform(self.X_train),
            color_by=color_by,
            title=title,
            x_label=x_label,
            y_label=y_label,
        )

    def _get_ellipse(self, x, y, ax, n_std: int = 3, edgecolor: str = "red"):
        cov = np.cov(x, y)
        if cov.shape != (2, 2) or np.any(np.isnan(cov)):
            return  # skip invalid data
        pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
        ell_radius_x = np.sqrt(1 + pearson)
        ell_radius_y = np.sqrt(1 - pearson)
        ellipse = Ellipse(
            (0, 0),
            width=ell_radius_x * 2,
            height=ell_radius_y * 2,
            edgecolor=edgecolor,
            facecolor="none",
            linewidth=2,
            alpha=0.5,
        )
        scale_x = np.std(x) * n_std
        scale_y = np.std(y) * n_std
        mean_x = np.mean(x)
        mean_y = np.mean(y)
        transf = (
            transforms.Affine2D()
            .rotate_deg(0)
            .scale(scale_x, scale_y)
            .translate(mean_x, mean_y)
        )
        ellipse.set_transform(transf + ax.transData)
        ax.add_patch(ellipse)

    def plot_residuals(
        self,
        color_by=None,
        label_by=None,
        title="Residuals",
    ):
        q_residuals = QResiduals(self.model)
        h_residuals = HotellingT2(self.model)

        q_train = q_residuals.fit_predict_residuals(self.X_train)
        h_train = h_residuals.fit_predict_residuals(self.X_train, y=None)

        if color_by is None:
            color_by = self.y_train

        fig, ax = plt.subplots(figsize=(5, 4))
        # Plot training data
        scatter = ax.scatter(
            h_train,
            q_train,
            c=color_by,
            cmap="turbo",
            edgecolor="k",
            s=50,
            label="Train",
        )

        # Plot test data
        if self.X_test is None:
            pass
        else:
            q_test = q_residuals.predict_residuals(self.X_test)
            h_test = h_residuals.predict_residuals(self.X_test, y=None)

            ax.scatter(
                h_test,
                q_test,
                c="blue",
                edgecolor="k",
                s=50,
                marker="s",
                label="Test",
            )

        ax.axhline(
            q_residuals.critical_value_,
            color="red",
            linestyle="--",
            label="Q Residuals Threshold",
        )
        ax.axvline(
            h_residuals.critical_value_,
            color="red",
            linestyle="--",
            label="Hotelling T2 Threshold",
        )

        # Add sample labels
        if label_by is None:
            pass
        else:
            for i, txt in enumerate(label_by):
                ax.annotate(
                    txt,
                    (h_train[i], q_train[i]),
                    textcoords="offset points",
                    xytext=(0, 5),
                    ha="center",
                )

        ax.set_title(title)
        ax.set_xlabel("Hotelling T2")
        ax.set_ylabel("Q Residuals")
        plt.colorbar(scatter, ax=ax, label="Color by (train)")
        ax.grid()
        plt.tight_layout()
        plt.show()
        return self
    
    def plot_prediction_results(self, color_by=None):
        """
        Plot prediction results for the PLS regression model.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if color_by is None:
            color_by = self.y_train
        else:
            color_by = np.asarray(color_by)
        fig, ax = plt.subplots(1, 3, figsize=(15, 5))

        # Parity plot
        ax[0].scatter(self.y_train, self.model.predict(self.X_train), c=color_by)
        if self.X_test is not None:
            ax[0].scatter(
                self.y_test,
                self.model.predict(self.X_test),
                c=color_by,
                marker="s",
            )
        ax[0].set_xlabel("True Values")
        ax[0].set_ylabel("Predicted Values")
        ax[0].set_title("Parity Plot")
        ax[0].plot(
            [self.y_train.min(), self.y_train.max()],
            [self.y_train.min(), self.y_train.max()],
            "k--",
        )

        # Residuals plot

        ax[1].scatter(self.y_train, self.model.predict(self.X_train) - self.y_train, c=color_by)
        if self.X_test is not None:
            ax[1].scatter(
                self.y_test,
                self.model.predict(self.X_test) - self.y_test,
                c='blue',
                marker="s",
            )
        ax[1].set_xlabel("True Values")
        ax[1].set_ylabel("Residuals")
        ax[1].set_title("Residuals Plot")

        # Histogram of residuals
        residuals = self.model.predict(self.X_train) - self.y_train
        ax[2].hist(residuals, bins=30, color="red", alpha=0.7)

        if self.X_test is not None: 
            residuals_test = self.model.predict(self.X_test) - self.y_test
            ax[2].hist(residuals_test, bins=30, color="blue", alpha=0.5)      

        ax[2].set_xlabel("Residuals")
        ax[2].set_ylabel("Frequency")
        ax[2].set_title("Histogram of Residuals")
        plt.tight_layout()
        plt.show()
        return self

