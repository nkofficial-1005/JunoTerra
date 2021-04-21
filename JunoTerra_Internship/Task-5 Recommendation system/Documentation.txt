# TASK 5: Recommendation System

### Module 1: Cities and Weather Data

The CSV file of cities in India was imported as a data frame using pandas. An open weather API was used to get the live weather data of the cities. The JSON data was extracted by defining a function and then normalized to convert JSON data to a data frame. EDA was performed to drop unnecessary columns and rename the essential columns. Similar steps were followed to extract the AQI data from Heroku cloud API. The final data was formed by joining the weather and AQI data. This data included city name, weather type, visibility of weather type, latitude, longitude, temperature, pressure, humidity, sea level, ground level, wind speed, wind degree, rain, AQI, CO, NO2, O3, PM10, PM25, SO2. 

### Module 2: Clustering Algorithm (preferably K-Means)

EDA was performed to check if the data is clean and ready to use. The Elbow method was used to determine an optimal number of clusters.

### Module 3: Venue Data 

Collecting best places using Foursquare’s API including Venue address, latitude, longitude, and category. The city data was used as Neighbourhood and one hot encoding was performed in the venue category column. The final data now was joined with the venue data to perform regression.

### Module 4: Modeling

Regress the data to find out which attribute can be taken as a dependent variable and get the scaled data using regression algorithms like ridge regression for building a recommendation system.

### Module 5: Content-based recommender system for city recommendation

a.define a function that will calculate cosine similarity between the user’s input city(ies) and the rest of the cities in the data frame.
b.then define a function that calls for the input of the user, takes the unweighted average of the cosine similarity values between each inputted city and the rest of the cities in the data frame, and returns a data frame with the top recommendations in descending order (default set at 10 recommendations)
