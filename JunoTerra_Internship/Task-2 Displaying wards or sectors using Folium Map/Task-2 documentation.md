# TASK 2: Displaying wards or sectors using Folium Map
### Module 1: Data Collection

The ward or sector data containing ward number and ward or sector name is fetched from various sources and saved as a CSV file.

### Module 2: Preparing the Dataframe

The csv file is read as pandas dataframe. State and country name is added to the data frame using aggregate operation.
```python
df = pd.read_csv("city_name_wards.csv", encoding= 'unicode_escape')
df['Country'] = 'India'
df['State'] = 'Gurugram'
df["location"] = df['Ward'] +", " + df['State'] +", " + df['Country']
```
A new location column is added joining the ward name, state, and country name. A function is defined to create two new columns, latitude and longitude; the columns are added after geocoding the location using GeoPy and Google Maps as Nominatim user agents.
```python
def findGeocode(location):   
    try: 
        geolocator = Nominatim(user_agent="Google Maps")
        return geolocator.geocode(location)
    except GeocoderTimedOut: 
        return findGeocode(location) 
```

### Module 3: Visualization

The data is cleaned by filling in the missing values and removing repetitions. The new data frame obtained after EDA is used to plot the location as markers in the folium map. 
The above task was carried out for four cities: Faridabad, Ghaziabad, Gurugram, and Noida.

