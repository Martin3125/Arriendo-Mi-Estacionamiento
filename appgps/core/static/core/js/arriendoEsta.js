
var map;
function initMap() {    

    var lati = document.getElementsByName("lat")[0].value;
    var long = document.getElementsByName("lng")[0].value;
    console.log(typeof lati,typeof long)
    const uluru = { lat: parseFloat(long) , lng: parseFloat(lati) };
    map = new google.maps.Map(document.getElementById('map'), {
        mapId: "b7011240b82da652",
        center: uluru,
        zoom: 16,

    });
    const marker = new google.maps.Marker({
        position: uluru,
        map: map,
        title: 'Estacionamiento'
    });


    function getCoords(position) {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;

        initialize(lat, lng);

    }
    function getError(err) {
        initialize(-33.69417055239359, -71.21368835681287);
    }
    google.maps.event.addListener(marker, 'position_changed', function () {
        getMarkerCoords(marker);
    });
    function getMarkerCoords(Marker) {
        var markerCoords = marker.getPosition();
        $('#inputLongitud').val(markerCoords.lng());
        $('#inputLatitud').val(markerCoords.lat());
    }
}
