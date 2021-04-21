# TASK 5: Recommendation System

### Module 1: Cities and Weather Data

The CSV file of cities in India was imported as a data frame using pandas. An open weather API was used to get the live weather data of the cities. The JSON data was extracted by defining a function and then normalized to convert JSON data to a data frame. 
```python
for i in range(len(df1)):
    url='http://api.openweathermap.org/data/2.5/weather?lat='+str(df1['Latitude'][i])+'&lon='+str(df1['Longitude'][i])+'&appid=7f9de45d1cc7764baf0aea8a915a7ff2'
    r = requests.get(url).json()
    temp_df1 = pd.json_normalize(r)
```
EDA was performed to drop unnecessary columns and rename the essential columns. Similar steps were followed to extract the AQI data from Heroku cloud API. The final data was formed by joining the weather and AQI data. This data included city name, weather type, visibility of weather type, latitude, longitude, temperature, pressure, humidity, sea level, ground level, wind speed, wind degree, rain, AQI, CO, NO2, O3, PM10, PM25, SO2. 

### Module 2: Clustering Algorithm (preferably K-Means)

EDA was performed to check if the data is clean and ready to use. The Elbow method was used to determine an optimal number of clusters.
```python
def elbow_kmeans_city(final_data, maxRange = 10):
    try:
        X_w = final_data.drop('City',1)
        X_w = MinMaxScaler().fit_transform(X_w)
    except:
        X_w = MinMaxScaler().fit_transform(final_data)


    Error =[]
    for i in range(1, maxRange+1):
        kmeans = KMeans(n_clusters = i).fit(X_w)
        kmeans.fit(X_w)
        Error.append(kmeans.inertia_)

    plt.plot(range(1, maxRange+1), Error)
    plt.title('Elbow method')
    plt.xlabel('No of clusters')
    plt.ylabel('Error')
    plt.show()
    
    return(X_w)
```

### Module 3: Venue Data 

Collecting best places using Foursquare’s API including Venue address, latitude, longitude, and category. The city data was used as Neighbourhood and one hot encoding was performed in the venue category column. 
```python
# one hot encoding
venues_onehot = pd.get_dummies(venues[['Venue Category']], prefix="", prefix_sep="")
```
The final data now was joined with the venue data to perform regression.

### Module 4: Modeling

Regress the data to find out which attribute can be taken as a dependent variable and get the scaled data using regression algorithms like ridge regression for building a recommendation system.
```python
from sklearn.linear_model import Ridge, LinearRegression
target = final_df[['AQI']]
target = MinMaxScaler().fit_transform(target)

predictors = final_df.drop(['City', 'weather','AQI','coord.lat','coord.lon'], axis=1)
X = MinMaxScaler().fit_transform(predictors)

reg = Ridge().fit(X, target)
reg.score(X, target)
```

### Module 5: Content-based recommender system for city recommendation

* define a function that will calculate cosine similarity between the user’s input city(ies) and the rest of the cities in the data frame.
* then define a function that calls for the input of the user, takes the unweighted average of the cosine similarity values between each inputted city and the rest of the cities in the data frame, and returns a data frame with the top recommendations in descending order (default set at 10 recommendations)
