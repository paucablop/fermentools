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


class PCAReport:
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
            model, model_type="pca"
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

    def plot_scores(
        self, color_by=None, title="PCA Scores", x_axis=1, y_axis=2, n_std=3
    ):
        X_train_pca = self.model.transform(self.X_train)

        if color_by is None:
            color_by = self.y_train

        fig, ax = plt.subplots(figsize=(5, 4))

        # Plot training data
        scatter = ax.scatter(
            X_train_pca[:, x_axis - 1],
            X_train_pca[:, y_axis - 1],
            c=color_by,
            cmap="turbo",
            edgecolor="k",
            s=50,
            label="Train",
        )

        # Add overall ellipse for training data
        self._get_ellipse(
            X_train_pca[:, x_axis - 1],
            X_train_pca[:, y_axis - 1],
            ax,
            n_std=n_std,
            edgecolor="red",
        )

        if self.X_test is None:
            pass
        else:
            X_test_pca = self.model.transform(self.X_test)
            # Plot test data
            ax.scatter(
                X_test_pca[:, x_axis - 1],
                X_test_pca[:, y_axis - 1],
                c="blue",
                edgecolor="k",
                s=50,
                marker="s",
                label="Test",
            )

            # Add overall ellipse for test data
            self._get_ellipse(
                X_test_pca[:, x_axis - 1],
                X_test_pca[:, y_axis - 1],
                ax,
                edgecolor="blue",
            )

        ax.set_title(title)
        ax.set_xlabel(f"PC{x_axis}")
        ax.set_ylabel(f"PC{y_axis}")
        plt.colorbar(scatter, ax=ax, label="Color by (train)")
        ax.legend()
        ax.grid()
        plt.tight_layout()
        plt.show()
        return self

    def plot_loadings(self, title="PCA Loadings"):
        loadings = self.estimator.components_.T

        if self.cut_wavenumbers is not None:
            wavenumbers = self.cut_wavenumbers
        else:
            wavenumbers = self.wavenumbers

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(wavenumbers, loadings)
        ax.set_title(title)
        ax.set_xlabel("Features")
        ax.set_ylabel("Loadings")
        ax.legend([f"PC{i + 1}" for i in range(loadings.shape[1])])
        ax.grid()
        plt.tight_layout()
        plt.show()
        return self

    def plot_scree(self, title="Cumulative Explained Variance"):
        explained_variance = self.estimator.explained_variance_ratio_
        cumulative_variance = np.cumsum(explained_variance)

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(
            range(1, len(explained_variance) + 1),
            explained_variance,
            marker="o",
            color="blue",
        )
        ax.bar(
            range(1, len(cumulative_variance) + 1),
            cumulative_variance,
            alpha=0.5,
            color="orange",
        )
        ax.set_title(title)
        ax.set_xlabel("Principal Component")
        ax.set_ylabel("Cumulative Explained Variance Ratio")
        ax.grid()
        plt.tight_layout()
        plt.show()
        return self

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
