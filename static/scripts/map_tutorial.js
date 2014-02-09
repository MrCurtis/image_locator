function onMapClick(e)
{
    var marker = L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);
    alert([e.latlng.lat, e.latlng.lng]);
}

function addMarker(lattitude, longtitude, status)
{   
    if (status == 'I')
    {
        var circle = L.circle([lattitude, longtitude], 500, {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5
        }).addTo(map);
    }
    else if (status == 'N')
    {
        var circle = L.circle([lattitude, longtitude], 500, {
        color: 'blue',
        fillColor: 'blue',
        fillOpacity: 0.5
        }).addTo(map);
    }
}

var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer("http://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
}).addTo(map);

map.on('click', onMapClick);


