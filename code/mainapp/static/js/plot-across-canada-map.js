function plotAcrossCanadaMap(data){
	var mymap = L.map('sitesDataMap').setView([62.0, -96.0], 3);
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
		attribution: '<a href="https://www.openstreetmap.org/">OpenStreetMap</a> | <a href="https://www.mapbox.com/">Mapbox</a>',
		maxZoom: 18,
		id: 'mapbox.streets',
		accessToken: 'pk.eyJ1IjoidmlzbWF5aHIiLCJhIjoiY2syZXZ3ZjhrMGUxMjNib2Z1dnpoem5sZCJ9.vhBE1EO3Lxa6TJBy5XyaqQ'
	}).addTo(mymap);
	var jsonData = data;

	var rows = parseInt(jsonData['grid_dimensions']['rows']);
	var columns = parseInt(jsonData['grid_dimensions']['columns']);

	var maxValue = 0;
	for(i=0; i<jsonData['across_canada_data'].length; i++){
		if(jsonData['across_canada_data'][i]['value'] > maxValue){
			maxValue = jsonData['across_canada_data'][i]['value'];
		}
	}

	var canadaData = jsonData['across_canada_data'];
	var r = 0;
	var c = 0;

	for(r=0; r < rows-1; r++){
		for(c=0; c < columns-1; c++){
			var p1 = (r*columns) + c;
			var p2 = (r*columns) + c + 1;
			var p3 = ((r+1)*columns) + c + 1;
			var p4 = ((r+1)*columns) + c;

			polygonBoundary = [[canadaData[p1]['lat'], canadaData[p1]['lon']],
								[canadaData[p2]['lat'], canadaData[p2]['lon']],
								[canadaData[p3]['lat'], canadaData[p3]['lon']],
								[canadaData[p4]['lat'], canadaData[p4]['lon']]];

			var val = parseFloat(canadaData[p1]['value']);
			var polygon = L.polygon(polygonBoundary, {color: polygonOutlineColour(val/maxValue), 
				fillColor: polygonFillColour(val/maxValue), stroke: false, fillOpacity: 0.4}).addTo(mymap);

			popupMessage = "Lat: " + canadaData[p1]['lat'] + "\nlon: " + canadaData[p1]['lon'] + "\nVariation (dB/dt): " + val;

			polygon.bindPopup(popupMessage);

		    polygon.on('mouseover', function (e) {
		        this.openPopup();
		    });
	        polygon.on('mouseout', function (e) {
	            this.closePopup();
	        });		

		}
		c = 0;
	}

}

function polygonOutlineColour(maxValue){
	if(maxValue < 0.2){
		return('blue');
	} else if(maxValue < 0.4){
		return('lime');
	} else if (maxValue < 0.7){
		return('yellow');
	} else return('red');
}

function polygonFillColour(maxValue){
	if(maxValue < 0.2){
		return('blue');
	} else if(maxValue < 0.4){
		return('lime');
	} else if (maxValue < 0.7){
		return('yellow');
	} else return('red');
}