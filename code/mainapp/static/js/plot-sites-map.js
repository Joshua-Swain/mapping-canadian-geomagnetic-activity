function plotSitesMap(data){
	var mymap = L.map('sitesDataMap').setView([62.0, -96.0], 3);
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
		attribution: '<a href="https://www.openstreetmap.org/">OpenStreetMap</a> | <a href="https://www.mapbox.com/">Mapbox</a>',
		maxZoom: 18,
		id: 'mapbox.streets',
		accessToken: 'pk.eyJ1IjoidmlzbWF5aHIiLCJhIjoiY2syZXZ3ZjhrMGUxMjNib2Z1dnpoem5sZCJ9.vhBE1EO3Lxa6TJBy5XyaqQ'
	}).addTo(mymap);
	var jsonData = data;
	var sites_data = jsonData['sites_data']
	for(row=0; row < sites_data.length; row++){
		site = sites_data[row]['name'];
		value = parseFloat(sites_data[row]['value']);
		latitude = parseFloat(sites_data[row]['lat']);
		longitude = parseFloat(sites_data[row]['lon']);

		var circle = L.circle([latitude, longitude], {
			color: circleOutlineColour(site),
			fillColor: circleFillColour(site),
			fillOpacity: 0.6,
			radius: value * 2000
		}).addTo(mymap);

		circle.bindPopup("Magnetic field variation (dB/dt) at " + site + ": " + value);

        circle.on('mouseover', function (e) {
            this.openPopup();
        });
        circle.on('mouseout', function (e) {
            this.closePopup();
        });		
	}
}

function circleOutlineColour(site){
	if(site === "MEA"){
		return("red")
	} else {
		return("green")
	}
}

function circleFillColour(site){
	if(site === "MEA"){
		return("#f03")
	} else {
		return("#36BF1D")
	}								
}
