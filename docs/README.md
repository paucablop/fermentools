# Python Documentation

## Classes

**[PCAReport](PCAReport.md)**: 

**[PLSRegressionReport](PLSRegressionReport.md)**: 

**[YeastModel](YeastModel.md)**: 

**[MassBalance](MassBalance.md)**: 

**[RangeCut](RangeCut.md)**: Cuts a dataframe selecting the wavenumbers between start and end. 

**[Derivative](Derivative.md)**: Calculates the derivative of a each row in a dataframe using the Savitzky-Golay filter. 

**[ExtendedKalmanFilter](ExtendedKalmanFilter.md)**: 


## Functions

### plot_pls_fermentation


Plots the predicted concentration and the reference hplc measurements. 
#### Parameters
name | description | default
--- | --- | ---
prediction | load the predictions. | 
fermentation_hplc | load the reference hplc measurements. | 





### plot_pls_training


Plots the PLS predictions and the reference hplc measurements for the training set. 
#### Parameters
name | description | default
--- | --- | ---
predictions | predicted concentrations. | 
reference | reference hplc measurements. | 





### plot_spectra


Plots spectra. 
#### Parameters
name | description | default
--- | --- | ---
spectra | dataframe containing the spectra with the wavenumbers as columns. | 
title | title of plot | 
xlabel | x-axis label | 
ylabel | y-axis label | 





### plot_mechanistic_fermentation


Plots the predicted concentration and the reference hplc measurements. 
#### Parameters
name | description | default
--- | --- | ---
prediction | load the predictions. | 
fermentation_hplc | load the reference hplc measurements. | 
time |  | 
concentrations |  | 





### load_training_data


Loads the training data. 




### load_fermentation_spectra_data


Loads the fermentation data. 




### load_fermentation_hplc_data


Loads the fermentation data. 




### load_filtered_fluorescence_data


returns the emission - excitation matrix for the filtered data 




### load_unfiltered_fluorescence_data


returns the emission - excitation matrix for the filtered data 




### extract_and_validate_model


Validate and extract a PCA or PLS model, optionally from a pipeline.   
This function checks whether the provided model or the final step in a pipeline is of the expected type (`PCA` or `PLSRegression`) and whether it has been fitted. It also separates any preceding pipeline steps (transformers) from the estimator.   
Parameters ---------- model : BaseEstimator or Pipeline A fitted scikit-learn estimator or a Pipeline containing a PCA or PLSRegression model as the final step.   
model_type : {'pca', 'pls'} The expected type of model. Must be one of 'pca' or 'pls'.   
Returns ------- transformer : Pipeline or None A pipeline containing all steps before the final estimator if the input is a Pipeline. `None` if the input is not a pipeline.   
estimator : PCA or PLSRegression The validated and fitted PCA or PLSRegression estimator.   
Raises ------ ValueError If `model_type` is not 'pca' or 'pls'.   
TypeError If the final model is not of the expected type.   
NotFittedError If the estimator has not been fitted yet. 
#### Parameters
name | description | default
--- | --- | ---
model |  | 
model_type |  | 





### get_cut_wavenumbers_from_pipeline


Retrieve the `cut_wavenumbers` attribute from a 'rangecut' step in a Pipeline, if present.   
Parameters ---------- pipeline : Pipeline A scikit-learn Pipeline object.   
Returns ------- cut_wavenumbers : Any or None The `cut_wavenumbers` attribute from the 'rangecut' step, or None if the step is absent. 
#### Parameters
name | description | default
--- | --- | ---
pipeline |  | 





### plot_spectra


Plot spectra with optional color coding based on a scalar array.   
Parameters ---------- x : ArrayLike The x-axis data (e.g., wavenumbers), shape (n_features,) y : ArrayLike The y-axis data (e.g., intensity values), shape (n_samples, n_features) color_by : Optional[ArrayLike], optional Optional array of shape (n_samples,) for color coding the lines. title : str, optional Title of the plot (default is "Spectra"). x_label : str, optional Label for the x-axis (default is "Wavenumber"). y_label : str, optional Label for the y-axis (default is "Intensity").   
Returns ------- fig : matplotlib.figure.Figure The figure object. ax : matplotlib.axes._axes.Axes The axes object. 
#### Parameters
name | description | default
--- | --- | ---
x |  | 
y |  | 
color_by |  | None
title |  | "Spectra"
x_label |  | "Wavenumber"
y_label |  | "Intensity"





### cross_validation


Performs cross-validation on the data. By default it performs a leave-one-out cross-validation. 
#### Parameters
name | description | default
--- | --- | ---
X | spectra dataframe containing the spectra with the wavenumbers as columns. | 
y | dataframe containing the reference hplc measurements. | 





### load_pls_glucose_model







### test_range_cut


Test the range cut. 




### test_derivate


Test the derivative. 




### test_ir_train_loadings


Test the loading of the training data. 




### test_ir_fermentation_loadings


Test the loading of the fermentation data. 




### test_fluorescence_loadings


Test the loading of the fluorescence data 



