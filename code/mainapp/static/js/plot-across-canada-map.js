function plotAcrossCanadaMap(data){
	console.log("Across Canada!")
	var mymap = L.map('sitesDataMap').setView([62.0, -96.0], 3);
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
		attribution: '<a href="https://www.openstreetmap.org/">OpenStreetMap</a> | <a href="https://www.mapbox.com/">Mapbox</a>',
		maxZoom: 18,
		id: 'mapbox.streets',
		accessToken: 'pk.eyJ1IjoidmlzbWF5aHIiLCJhIjoiY2syZXZ3ZjhrMGUxMjNib2Z1dnpoem5sZCJ9.vhBE1EO3Lxa6TJBy5XyaqQ'
	}).addTo(mymap);
	var jsonData = data;

}