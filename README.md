# Sentiment Analysis of Climate Related Tweets

This repository takes time series data from an air quality monitoring station in China and forecasts the ozone levels in the coming hour given the previous day and then the next day given the past week. 

## Data

The data was acquired by personal communication with the author of: https://iopscience.iop.org/article/10.1088/1748-9326/aae718/pdf. There are over 50,000 lines in the datafile so is not included in the repository. 

## Files

- O3_Prediction.ipynb: ipython notebook which takes the original data, adds features to include seasonality on the yearly, monthly, daily scale. Then I create two networks using LSTM layers (a type used in recurrent neural networks).

## Use

To use this notebook and files, you need to download the data from the link above and install the anaconda environment provided using: 

`conda env create -f environment.yml`

The data can be acquired upon personal request. 




