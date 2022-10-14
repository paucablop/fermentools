# Python Documentation

## Classes

**[YeastModel](YeastModel.md)**: 

**[MassBalance](MassBalance.md)**: 

**[RangeCut](RangeCut.md)**: Cuts a dataframe selecting the wavenumbers between start and end. 

**[Derivative](Derivative.md)**: Calculates the derivative of a each row in a dataframe using the Savitzky-Golay filter. 

**[ExtendedKalmanFilter](ExtendedKalmanFilter.md)**: 


## Functions

### test_ir_train_loadings


Test the loading of the training data. 




### test_ir_fermentation_loadings


Test the loading of the fermentation data. 




### test_fluorescence_loadings


Test the loading of the fluorescence data 




### test_range_cut


Test the range cut. 




### test_derivate


Test the derivative. 




### load_pls_glucose_model







### cross_validation


Performs cross-validation on the data. By default it performs a leave-one-out cross-validation. 
#### Parameters
name | description | default
--- | --- | ---
X | spectra dataframe containing the spectra with the wavenumbers as columns. | 
y | dataframe containing the reference hplc measurements. | 





### plot_mechanistic_fermentation


Plots the predicted concentration and the reference hplc measurements. 
#### Parameters
name | description | default
--- | --- | ---
prediction | load the predictions. | 
fermentation_hplc | load the reference hplc measurements. | 
time |  | 
concentrations |  | 





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





### load_filtered_fluorescence_data


returns the emission - excitation matrix for the filtered data 




### load_unfiltered_fluorescence_data


returns the emission - excitation matrix for the filtered data 




### load_training_data


Loads the training data. 




### load_fermentation_spectra_data


Loads the fermentation data. 




### load_fermentation_hplc_data


Loads the fermentation data. 



