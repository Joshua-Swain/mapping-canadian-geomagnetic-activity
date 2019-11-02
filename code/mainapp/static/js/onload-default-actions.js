function clickSitesMapBtn(){
	console.log("inside click btn func");
	document.getElementById('sitesMapBtn').checked = true;
	console.log("Called plot map");
	plotMap();
}