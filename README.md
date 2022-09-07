# dtu.prosys

## About this project 🚀
This project intends to be a didactic tool to teach spectroscopy and chemometrics in the context of fermentation technology. During my studies, I often felt that many courses were theory-based only due to the limited access to real-world data. For this reason, I have decided to distribute the data I generated during my studies hoping to improve the learning experience of future students. 

This module contains:
 - Training data (spectra of different samples and the glucose concentration). 
 - Fermentation spectra (spectra measured in _real-time_ every minute).
 - Fermentation HPLC data (measured off-line every hour).
 - Common preprocessing operations used in chemometrics.
 - Workflow to train partial least squares (PLS) models.
 - Plotting functions for time-series and spectral data.

These functions can be used as a starting point for the, but more advanced users are encouradged to explore other packages to play with this data (e.g., ```scikit-learn```, or ```scipy```). 

## About the data 📈
This project provides two datasets (a training and a validation set). Both data sets were recorded at the Technical University of Denmark, at the PROSYS research center (department of Chemical and Biochemical engineering) during 2019. More information about the dataset can be found in the following article [Transforming data to information: A parallel hybrid model for real-time state estimation in lignocellulosic ethanol fermentation](https://onlinelibrary.wiley.com/doi/10.1002/bit.27586)

### The training set
The training set contains the spectra of 20 semi-synthetic samples and their reference glucose concentration measured with high performance liquid chromatography (HPLC). The spectra were measured using attenuated total refractance mid infrared (ATR-MIR) spectroscopy.

### Validation set
The validation contains spectra measured every minute during a lignocellulose to ethanol fermentation. These spectra were collected in _real-time_ using the same ATR-MIR instrument, connected to a flow-cell. Moreover, the extracellular concentrations of glucose, xylose, ethanol, furfural and acetic acid were also measured every hour using HPLC.  

## Installation 💻
### Dependencies
This project is build targetting Python >= 3.7 to ensure compatibility with Google Colab.

### User installation ```pip```

```
pip install -U dtuprosys
```

## Quick start 🏁
A complete example of can be found in the [```example.ipynb```](https://github.com/paucablop/dtu.prosys/blob/main/example.ipynb). The raw data can be conviniently accessed using as the following commands:

```
from dtuprosys.datasets import load_train_data, load_fermentation_data
```
to access the training data

```
train_spectra, train_hplc = load_train_data()
```
to access the validation data:
```
fermentation_spectra, fermentation_hplc = load_fermentation_data()
``` 
