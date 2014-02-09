
var setupKeyboard = function(){
	
	console.log("--- keyboard setup ---");

	document.onkeydown = function(e){
		
			//leftKeyPress
			if(e.keyCode == '39'){
				console.log('NEXT');
				document.getElementById("triageForm").submit();
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
};
