
var setupKeyboard = function(){
	
	console.log("--- keyboard setup ---");

	document.onkeydown = function(e){
		
			//leftKeyPress
			if(e.keyCode == '39'){
				console.log('NEXT');
				document.getElementById("testForm").submit();
			};
			
			//--- STATUS ---
			
			//Water
			if(e.keyCode =='49'){
			   if(document.getElementById("id_water").checked == false) {
					document.getElementById("id_water").checked = true;
				}
				else{ document.getElementById("id_water").checked = false;
				}
			};
			
			//food
			if((e.keyCode =='50')){
				if(document.getElementById("id_food").checked == false) {
					document.getElementById("id_food").checked = true;
				}
				else{ document.getElementById("id_food").checked = false;
				}
			};
			
			//shelter
			if(e.keyCode =='51'){
			   if(document.getElementById("id_shelter").checked == false) {
					document.getElementById("id_shelter").checked = true;
				}
				else{ document.getElementById("id_shelter").checked = false;
				}
			};
			
			//medical
			if(e.keyCode =='52'){
			   if(document.getElementById("id_medicine").checked == false) {
					document.getElementById("id_medicine").checked = true;
				}
				else{ document.getElementById("id_medicine").checked = false;
				}
			};
			
			//protection
			if(e.keyCode =='53'){
			   if(document.getElementById("id_protection").checked == false) {
					document.getElementById("id_protection").checked = true;
				}
				else{ document.getElementById("id_protection").checked = false;
				}
			};
			
		};

}

// on initialisation
window.onload = function() {


	
	console.log("--- Initialising ---");

    setupKeyboard();

	//	Create the map
	map = new OpenLayers.Map("mapView");
		
	map.addLayer(new OpenLayers.Layer.OSM());
		
	//	Load image points from KML file
	var kmllayer = new OpenLayers.Layer.Vector("KML", {
			strategies: [new OpenLayers.Strategy.Fixed()],
			protocol: new OpenLayers.Protocol.HTTP({
				url: "/static/images/2013-07-25 19-54-04.tlog.kml",
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
//	navigator.geolocation.getCurrentPosition(function(position) {
//		var lonLat = new OpenLayers.LonLat(position.coords.longitude,position.coords.latitude)
//			.transform(
//				new OpenLayers.Projection("EPSG:4326"),	//transform from WGS 1984
//				map.getProjectionObject()				//to Spherical Mercator Projection
//			);
//		map.setCenter(lonLat, 1 // Zoom out to global level so user can zoom in on area of interest.
//		);
//	});
 
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
