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

	L.control.legend({
	    items: [
	        {color: '#E74C3C', label: (parseFloat(0.7*maxValue).toFixed(2)) + " - " + (parseFloat(maxValue).toFixed(2)) },
	        {color: '#F39C12', label: (parseFloat(0.4*maxValue).toFixed(2)) + " - " + (parseFloat(0.699*maxValue).toFixed(2))},
	        {color: '#2ECC71', label: (parseFloat(0.2*maxValue).toFixed(2)) + " - " + (parseFloat(maxValue*0.399).toFixed(2))},
	        {color: '#2E86C1', label: 0 + " - " + (parseFloat(maxValue*0.2).toFixed(2))}
	    ],
	    collapsed: false,
	    // insert different label for the collapsed legend button.
	}).addTo(mymap);

}

function polygonFillColour(val) {
    return val > 0.7  ? '#E74C3C' :
           val > 0.4  ? '#F39C12' :
           val > 0.2  ? '#2ECC71' :
           			   '#2E86C1' ;
}

function polygonOutlineColour(val){
	if(val < 0.2){
		return('#2E86C1 ');
	} else if(val < 0.4){
		return('#2ECC71');
	} else if (val < 0.7){
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