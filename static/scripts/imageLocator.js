
//Initialisation

var changeImage= function(){
	//document.imageView.src = "images/01.jpg"
}


window.onload = function(){

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
	
}