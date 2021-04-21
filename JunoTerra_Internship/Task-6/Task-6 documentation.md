# TASK 6: Calling API 

## API Extraction       

1. Earthquake API was extracted for the past 5 days using USGS documentations.
2. World Population was extracted through Census Bureau datasets.
3. Covid cases of India were extracted state-wise using the covid19india dataset.

## Extraction and EDA                                                           

### Module 1: Data Preparation

Important libraries were imported and JSON formatted API was extracted in the code. The pandas.json_normalize() library was used to convert the data into a data frame. The columns which weren't necessary were dropped and were prepared for Exploratory Data Analysis.

### Module 2: Exploratory Data Analysis

A profile report was prepared by importing ProfileReport from the pandas_profiling library. Correlation and covariance of the data were calculated and seaborn heatmaps were plotted of the correlated data. Spearman's correlation was also calculated for all the value parameters. 

### Module 3: Maximum, Minimum, and Average Values

Correlation and covariance of parameters based on their maximum, minimum, and average values were calculated. The maximum, minimum, and average values were extracted using the max(), min(), and mean() function. The time for maximum value was extracted using get_value() function. Seaborn heatmaps were plotted of the correlated data. Spearman's correlation was also calculated for all the value parameters.
