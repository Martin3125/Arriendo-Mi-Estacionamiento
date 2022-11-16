
// var map;
// function initMap() {    

//     var lati = document.getElementsByName("lat")[0].value;
//     var long = document.getElementsByName("lng")[0].value;
//     console.log(lati, long)
//     const uluru = { lat:-33.69417055239359 , lng:  -71.21368835681287 };
//     map = new google.maps.Map(document.getElementById('map'), {
//         mapId: "b7011240b82da652",
//         center: uluru,
//         zoom: 16,

//     });
//     const marker = new google.maps.Marker({
//         position: uluru,
//         map: map,
//         title: 'Estacionamiento'
//     });


//     function getCoords(position) {
//         var lat = position.coords.latitude;
//         var lng = position.coords.longitude;

//         initialize(lati, long);

//     }
//     function getError(err) {
//         initialize(-33.69417055239359, -71.21368835681287);
//     }
//     google.maps.event.addListener(marker, 'position_changed', function () {
//         getMarkerCoords(marker);
//     });
//     function getMarkerCoords(Marker) {
//         var markerCoords = marker.getPosition();
//         $('#inputLongitud').val(markerCoords.lng());
//         $('#inputLatitud').val(markerCoords.lat());
//     }
// }

//----------------------------------------------------------------------------------

// var map;
// function initMap() {
//     const listarUbicaciones = async (nombre) => {
//         try {
//             const response = await fetch(`./obtener`);
//             const data = await response.json();
//             console.log(data);
//             if (data.message === "Success") {
//                 let opciones = ``;

//                 data.ubicaciones.forEach((ubicacion) => {

//                     var marcadores = [
//                         [ubicacion.nombre, ubicacion.lng, ubicacion.lat]

//                     ];
//                     var infowindow = new google.maps.InfoWindow({
//                         content: contentString,
//                         ariaLabel: "Uluru"
//                     });
                        
//                     var marker, i;
//                     for (i = 0; i < marcadores.length; i++) {
//                         marker = new google.maps.Marker({
//                             position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2]),
//                             map: map,
//                             title: marcadores[i][0],
//                         });
//                         google.maps.event.addListener(marker, 'click', (function (marker, i) {
//                             return function () {
//                                 // infowindow.setContent(marcadores[i][0]);
//                                 infowindow.open(map, marker);
//                                 infowindow.open({
//                                 anchor: marker,
//                                 map,
//                             });
//                             }
//                         })(marker, i));
//                     }
//                 });
//                 cboUbicacion.innerHTML = opciones;

//             } else {
//                 alert("Estacionamientos no encontrados...");
//             }
//         } catch (error) {
//             console.log(error);
//         }
//     };
//             var lati = document.getElementsByName("lat")[0].value;
//             var long = document.getElementsByName("lng")[0].value;
//             console.log(lati, long)
//             const uluru = { lat: position.coords.latitude, lng: position.coords.longitude };
//             map = new google.maps.Map(document.getElementById('map'), {
//                 mapId: "b7011240b82da652",
//                 center: uluru,
//                 zoom: 15,
//             });
//             const marker = new google.maps.Marker({
//                 position: uluru,
//                 map: map,
//                 title: 'Arrastrame'
//             });
//         })
//     }
//     let mark = [];
//     const cargaInicial = async () => {
//         await listarUbicaciones();

//         // cboUbicacion.addEventListener("change", (event) => {
//         //     mostrarUbicacion(event.target.value);
//         // });
//     };

//     window.addEventListener("load", async () => {
//         await cargaInicial();
//     });

// }

//     if ("geolocation" in navigator) {
//         navigator.geolocation.getCurrentPosition(function (position) {
//             var lati = document.getElementsByName("lat")[0].value;
//             var long = document.getElementsByName("lng")[0].value;
//             console.log(lati, long)
//             // const uluru = { lat: lati, lng: long }; 

//                 map = new google.maps.Map(document.getElementById('map'), {
//                     mapId: "b7011240b82da652",
//                     center: lati,long,
//                     zoom: 14,
//                 });
//                 const marker = new google.maps.Marker({
//                     position: uluru,
//                     map: map,
//                     draggable: true,
//                     title: 'Arrastrame'
//                 });
//                 function getCoords(position) {
//                     var lat = lati;
//                     var lng = long;

//                     initialize(lat, lng);

//                 }
//                 function getError(err) {
//                     initialize(-33.69417055239359, -71.21368835681287);
//                 }
//                 google.maps.event.addListener(marker, 'position_changed', function () {
//                     getMarkerCoords(marker);
//                 });
//                 function getMarkerCoords(Marker) {
//                     var markerCoords = marker.getPosition();
//                     $('#inputLongitud').val(markerCoords.lng());
//                     $('#inputLatitud').val(markerCoords.lat());
//                 }
//         }); 
//     }



// }
// google.maps.event.addDomListener(window, 'load', initialize);
    // let mark = [];
    // const listarUbicaciones = async (nombre) => {
    //     // try {
    //         var nombre = $('#inputNombre').val();
    //         const response = await fetch(`./obtenerArriendo`,nombre);
    //         const data = await response.json();
    //         console.log(data);
    // if (data.message === "Success") {
    //     let opciones = ``;

    //     data.ubicaciones.forEach((ubicacion) => {
    //         var marcadores = [
    //             [ubicacion.nombre, ubicacion.lng, ubicacion.lat]

    //         ];
    //         var map = new google.maps.Map(document.getElementById('mapa'), {
    //             zoom: 7,
    //             center: new google.maps.LatLng(ubicacion.lng, ubicacion.lat),
    //             mapTypeId: google.maps.MapTypeId.ROADMAP
    //         });
    //         var infowindow = new google.maps.InfoWindow();
    //         var marker, i;
    //     })
    //     google.maps.event.addDomListener(window, 'load', initialize);
    // } else {
    //     alert("Estacionamientos no encontrados...");
    //     // }
    // } catch (error) {
    //     console.log(error);
    // }


//     if ("geolocation" in navigator) {
//         navigator.geolocation.getCurrentPosition(function (position) {
//             const uluru = { lat: position.coords.latitude, lng: position.coords.longitude };
//             let mark = [];
//             const listarUbicaciones = async (nombre) => {


//                 const response = await fetch(`./obtener`);
//                 const data = await response.json();
//                 console.log(data);
//                 if (data.message === "Success") {
//                     let opciones = ``;

//                     data.ubicaciones.forEach((ubicacion) => {

//                         var marcadores = [
//                             [ubicacion.nombre, ubicacion.lng, ubicacion.lat]

//                         ];
//                     });
//                     var map = new google.maps.Map(document.getElementById('map'), {
//                         zoom: 7,
//                         center: new google.maps.LatLng(),
//                         mapTypeId: google.maps.MapTypeId.ROADMAP
//                     });
//                     var infowindow = new google.maps.InfoWindow();
//                     var marker, i;
//                     for (i = 0; i < marcadores.length; i++) {
//                         marker = new google.maps.Marker({
//                             position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2]),
//                             map: map
//                         });
//                         google.maps.event.addListener(marker, 'click', (function (marker, i) {
//                             return function () {
//                                 infowindow.setContent(marcadores[i][0]);
//                                 infowindow.open(map, marker);
//                             }
//                         })(marker, i));

//                     }


//                 }
//             }

//         });
//
//     }




