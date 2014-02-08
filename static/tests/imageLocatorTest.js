var iL = new onload;

describe ("An instance", function (){

	it("current image object has all data", function() {
		expect(iL.loadedImage.src).toBeTruthy();
		expect(iL.loadedImage.lat).toBeTruthy();
		expect(iL.loadedImage.lon).toBeTruthy();
	});
});
