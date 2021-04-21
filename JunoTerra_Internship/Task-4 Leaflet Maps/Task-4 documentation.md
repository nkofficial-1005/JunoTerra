# TASK 4: Choropleth Map - Leaflet

An HTML script was written to develop a demo web application that could display the localities in Delhi. The values of those localities included their area measured in square feet and their price per square foot. This data was extracted for a specific date and was saved as a CSV file. This data was then converted into geojson format to the polygonal geometry. 

The Mapbox API was used to get the tile type and openstreet map.

```
	var map = L.map('map').setView([28.70, 77.10], 10);

	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
			'Imagery ? <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/light-v9',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(map);
```

The JSON data was used in the HTML script along with the Map attributes to give shape to a Leaflet Map. The script was developed in a manner to create a hover-over map with a color scale. 

The HTML script was further deployed as a Heroku web application and the screenshot of the output is displayed below.

![leaflet](https://github.com/nkofficial-1005/JunoTerra/blob/master/JunoTerra_Internship/images/leaflet.png)

![hover](https://github.com/nkofficial-1005/JunoTerra/blob/master/JunoTerra_Internship/images/leaflet_hover.png)
