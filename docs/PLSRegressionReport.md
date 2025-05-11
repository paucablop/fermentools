# PLSRegressionReport




## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
model |  | 
X_train |  | 
y_train |  | 
X_test |  | None
y_test |  | None
wavenumbers |  | None





### plot_data


Plot spectra with optional color coding.   
Parameters ---------- color_by : Optional[ArrayLike] Optional array for color coding the points. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
color_by |  | None
title |  | "Spectra"
x_label |  | "Wavenumber"
y_label |  | "Intensity"





### plot_preprocessed_data


Plot preprocessed spectra with optional color coding.   
Parameters ---------- color_by : Optional[ArrayLike] Optional array for color coding the points. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
color_by |  | None
title |  | "Spectra"
x_label |  | "Wavenumber"
y_label |  | "Intensity"





### _get_ellipse




#### Parameters
name | description | default
--- | --- | ---
self |  | 
x |  | 
y |  | 
ax |  | 
n_std |  | 3
edgecolor |  | "red"





### plot_residuals




#### Parameters
name | description | default
--- | --- | ---
self |  | 
color_by |  | None
label_by |  | None
title |  | "Residuals"





### plot_prediction_results


Plot prediction results for the PLS regression model.   
Parameters ---------- None   
Returns ------- None 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
color_by |  | None




