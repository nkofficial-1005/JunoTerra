# TASK 6: Calling API 

## API Extraction       

1. Earthquake API was extracted for the past 5 days using USGS documentations.

[Eathquake API Data](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlatitude=8&maxlatitude=37&minlongitude=68&maxlongitude=97&starttime=2021-02-14T00:00:00&endtime=2021-02-19T00:00:00)

2. World Population was extracted through Census Bureau datasets.

[World Population](https://www.census.gov/popclock/data/fips_pop.json)

3. Covid cases of India were extracted state-wise using the covid19india dataset.

[Live COVID Data](https://api.covid19india.org/v4/min/data.min.json)

## Extraction and EDA                                                           

### Module 1: Data Preparation

Important libraries were imported and JSON formatted API was extracted in the code. The pandas.json_normalize() library was used to convert the data into a data frame.
```python
r = requests.get(url).json()
temp_df = pd.json_normalize(r)
```
The columns which weren't necessary were dropped and were prepared for Exploratory Data Analysis.

### Module 2: Exploratory Data Analysis

A profile report was prepared by importing ProfileReport from the pandas_profiling library. 
```python
from pandas_profiling import ProfileReport
profile = ProfileReport(activity,
                        title='Harmful components Report',
                        html={'style':{'full_width': True}})
profile.to_file('activity.html')
```
Correlation and covariance of the data were calculated and seaborn heatmaps were plotted of the correlated data. Spearman's correlation was also calculated for all the value parameters. 
```python
for i in activity.columns:
  for j in activity.columns:
    corr, _ = spearmanr(activity[i], activity[j])
    print(i, j, 'Spearmans correlation: %.3f' % corr)
```

### Module 3: Maximum, Minimum, and Average Values

Correlation and covariance of parameters based on their maximum, minimum, and average values were calculated. The maximum, minimum, and average values were extracted using the max(), min(), and mean() function. 
```python
for i in activity.columns.drop('Time'):
  maxValue = activity[i].max()
  minValue = activity[i].min()
  average = activity[i].mean()
  maxValueIndex = activity[i].idxmax()
```
The time for maximum value was extracted using get_value() function. 
```python
for i in df1['Index of MaxValue']:
  Time = activity._get_value(i, 0, takeable=True)
  print(Time)
```
Seaborn heatmaps were plotted of the correlated data. Spearman's correlation was also calculated for all the value parameters.
