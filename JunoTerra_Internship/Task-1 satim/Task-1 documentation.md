# TASK 1: SATIM
## (Web App for calculating the green percentage of user's location)
### Module 1: Extraction of Location

The location of a user is extracted using the input() function and then the location is converted to latitude and longitude, hence extracting the location coordinates.
```python
locator = Nominatim(user_agent= "Google Maps")
location = locator.geocode(input())
lat = location.latitude
longi = location.longitude
```
While in Flask web app, the relaxation was provided to user. The user has to just change the coordinates in the URL which was provided in the app route. Further, the predict function was defined to store the code.
```python
@app.route('/predict/<float(signed=True):lat>/<float(signed=True):longi>',methods=['GET','POST'])
```

### Module 2: Extraction of Satellite Image

The mercantile library is used to return the tile containing a given point. The point is extracted using the location coordinates with a distance of around one to two kilometers. The satellite image is extracted using the Mapbox API using the Map service of Mapbox APIs. The resultant image is then cropped centrally from XYZ coordinates. 

### Module 3: Extraction of Parameters

Opencv library is used to read the cropped image and NumPy library is used to calculate the lower green part and upper green part of the image. 
```python
img = cv2.imread("./static/crop.png")
lower_green = np.array([25, 52, 52])
upper_green = np.array([102, 255, 255])
```
The image with the resolution is then extracted. The green percentage of the total area is then calculated using the NumPy.sum() and NumPy.size() functions.
```python
green_perc = (np.sum(mask) / np.size(mask)) / 255
```
The above code is then deployed as a Flask web app API. The API is then deployed to a cloud platform Heroku as a web app named Satim. The latitude and longitude can be changed by the user to get the desired result.

