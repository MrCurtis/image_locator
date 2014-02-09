var map;

function addMarker(color, fillColor, radius)
{   
  return L.circle(map.getCenter(), radius, {
    color: color,
    //fillColor: fillColor || color,
    //fillOpacity: 0.5
  }).addTo(map);
}

function initMap(lat, lng) {
  map = L.map('map').setView([lat, lng], 14);

  L.tileLayer("http://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
      maxZoom: 18
  }).addTo(map);
  L.marker([lat, lng]).addTo(map);
}
