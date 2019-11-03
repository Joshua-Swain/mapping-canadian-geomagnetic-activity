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

			popupMessage = "Lat:" + canadaData[p1]['lat'] + " Lon:" + canadaData[p1]['lon'] + " Variation (dB/dt):" + val;
			popupMessage = "Magnetic field variation (dB/dt) at (" + canadaData[p1]['lat'] + "," + canadaData[p1]['lon'] + ") is: " + val;
			//popupMessage = "Variation(dB/dt) at (" + canadaData[p1]['lat'] + ""

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

	var legend = L.control({position: 'bottomleft'});

	legend.onAdd = function (mymap) {

	    var div = L.DomUtil.create('div', 'info legend'),
	    grades = [0, parseFloat(maxValue*0.199).toFixed(2), parseFloat(maxValue*0.399).toFixed(2), parseFloat(maxValue*0.699).toFixed(2), parseFloat(maxValue*0.7).toFixed(2)],
	    labels = [];

	    console.log("GRADES IS: " + grades);

	    // loop through our density intervals and generate a label with a colored square for each interval
	    for (var i = 0; i < grades.length; i++) {
	    	console.log("Color for: " + grades[i] + " is " + polygonFillColour(grades[i] + 0.1));
	        div.innerHTML +=
	            '<i style="background:' + polygonFillColour(grades[i] + 0.1) + '"></i> ' +
	            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
	}

	return div;
	};

	legend.addTo(mymap);

}

function polygonFillColour(d) {
    return d > 0.7 	? '#E74C3C' :
           d > 0.4  ? '#F39C12' :
           d > 0.2  ? '#2ECC71' :
           			  '#2E86C1' ;
}

function polygonOutlineColour(maxValue){
	if(maxValue < 0.2){
		return('#2E86C1 ');
	} else if(maxValue < 0.4){
		return('#2ECC71');
	} else if (maxValue < 0.7){
		return('#F39C12');
	} else return('#E74C3C');
}

/*function polygonFillColour(maxValue){
	if(maxValue < 0.2){
		return('#2E86C1 ');
	} else if(maxValue < 0.4){
		return('#2ECC71');
	} else if (maxValue < 0.7){
		return('#F39C12');
	} else return('#E74C3C');
}*/