
//Initialisation

var changeImage = function() {
	//document.imageView.src = "images/01.jpg"
};


window.onload = function() {

	//object literal for image data

	this.loadedImage = {
		src: "filePath",
		lat: 101010,
		lon: 1010101
	};
	
	//setup carousel
	$('.carousel').carousel();
	
	
	console.log("--- Initialising ---");

	//set the initial image
	this.loadedImage.src ="images/01.jpg";
	changeImage(this.loadedImage.src);

	//	Create the map
	map = new OpenLayers.Map("mapView");
		
	map.addLayer(new OpenLayers.Layer.OSM());
		
	//	Load image points from KML file
	var kmllayer = new OpenLayers.Layer.Vector("KML", {
			strategies: [new OpenLayers.Strategy.Fixed()],
			protocol: new OpenLayers.Protocol.HTTP({
				url: "./images/2013-07-25 19-54-04.tlog.kml",
				format: new OpenLayers.Format.KML({
					extractStyles: true,
					extractAttributes: true,
					maxDepth: 2
				})
			})
		});
	
	//	Add the KML to the map
	map.addLayer(kmllayer);
	
	//Set start centrepoint from device's location and zoom
	navigator.geolocation.getCurrentPosition(function(position) {
		var lonLat = new OpenLayers.LonLat(position.coords.longitude,position.coords.latitude)
			.transform(
				new OpenLayers.Projection("EPSG:4326"),	//transform from WGS 1984
				map.getProjectionObject()				//to Spherical Mercator Projection
			);
		map.setCenter(lonLat, 1 // Zoom out to global level so user can zoom in on area of interest.
		);
	});
 
	// Add a selector control to the kmllayer with popup functions
	var controls = {
		selector: new OpenLayers.Control.SelectFeature(kmllayer, { onSelect: createPopup, onUnselect: destroyPopup })
	};

	function createPopup(feature) {
		feature.popup = new OpenLayers.Popup.FramedCloud("pop",
			feature.geometry.getBounds().getCenterLonLat(),
			null,
			'<div class="markerContent"><h1>'+feature.attributes.description+'</h1></div>',
			null,
			true,
			function() { controls['selector'].unselectAll(); }
		);
//		feature.popup.closeOnMove = true;
		map.addPopup(feature.popup);
	}

	function destroyPopup(feature) {
		feature.popup.destroy();
		feature.popup = null;
	}
	
	map.addControl(controls['selector']);
	controls['selector'].activate();


	
};