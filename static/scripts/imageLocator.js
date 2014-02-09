var waterCircle, foodCircle, shelterCircle, medicalCircle, protectionCircle;
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
        waterCircle = addMarker('blue', '#33f', 100);
      } else {
        document.getElementById("id_water").checked = false;
        map.removeLayer(waterCircle);
      }
    };

    //food
    if((e.keyCode =='50')){
      if(document.getElementById("id_food").checked == false) {
        document.getElementById("id_food").checked = true;
        foodCircle = addMarker('green', '#3f3', 200);
      } else {
        document.getElementById("id_food").checked = false;
        map.removeLayer(foodCircle);
      }
    };

    //shelter
    if(e.keyCode =='51'){
      if(document.getElementById("id_shelter").checked == false) {
        document.getElementById("id_shelter").checked = true;
        shelterCircle = addMarker('black', '#333', 300);
      } else {
        document.getElementById("id_shelter").checked = false;
        map.removeLayer(shelterCircle);
      }
    };

    //medical
    if(e.keyCode =='52'){
      if(document.getElementById("id_medicine").checked == false) {
        document.getElementById("id_medicine").checked = true;
        medicalCircle = addMarker('red', '#f33', 400);
      } else {
        document.getElementById("id_medicine").checked = false;
        map.removeLayer(medicalCircle);
      }
    };

    //protection
    if(e.keyCode =='53'){
      if(document.getElementById("id_protection").checked == false) {
        document.getElementById("id_protection").checked = true;
        protectionCircle = addMarker('yellow', '#3ff', 500);
      } else {
        document.getElementById("id_protection").checked = false;
        map.removeLayer(protectionCircle);
      }
    };
  };
}

// on initialisation
window.onload = function() {
	console.log("--- Initialising ---");
  setupKeyboard();
}
