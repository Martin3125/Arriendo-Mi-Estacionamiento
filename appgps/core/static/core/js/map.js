
var map;
function initMap() {
    const uluru = { lat: -33.69417055239359, lng: -71.21368835681287 };
    map = new google.maps.Map(document.getElementById('map'), {
        mapId: "b7011240b82da652",
        center: uluru,
        zoom: 16,

    });
    const marker = new google.maps.Marker({
        position: uluru,
        map: map,
        draggable: true,
        title: 'Arrastrame'
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