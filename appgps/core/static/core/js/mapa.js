
// function iniciarMap(){
//     var coord = {lat:-34.5956145 ,lng: -58.4431949};
//     var map = new google.maps.Map(document.getElementById('map'),{
//       zoom: 10,
//       center: coord
//     });
//     var marker = new google.maps.Marker({
//       position: coord,
//       map: map
//     });
// }

// $(document).ready(function() {
    
//     google.maps.event.addDomListener(window, 'load', initMap);



    

      
// });      

// Initialize and add the map
// var map;
// function initMap() {
//   // The location of Uluru
//   const uluru = { lat: -25.344, lng: 131.031 };
//   // The map, centered at Uluru
//   const map = new google.maps.Map(document.getElementById("map"), {
//     zoom: 4,
//     center: uluru,
//   });
//   // The marker, positioned at Uluru
//   const marker = new google.maps.Marker({
//     position: uluru,
//     map: map,
//   });
//   var stylesArray = [
//     {
//       featureType: '',
//       elementType: '',
//       stylers: [
//         {color: ''},
//         {visibility: ''},
//         // Add any stylers you need.
//       ]
//     },
//     {
//       featureType: '',
//       // Add the stylers you need.
//     }
//   ]
// }

// window.initMap = initMap;

// $(document).ready(function(){
//   if (navigator.geolocation)
//   {
//       navigator.geolocation.getCurrentPosition(getCoords, getError);
//   }else{

//   }
//   var map;
//   function getCoords(position)
//   {
//       var lat = position.coords.latitude;
//       var lng = position.coords.longitude;

//       initialize(lat, lng);

//   }

//   function getError(err)
//   {
//       initialize(-33.69417055239359, -71.21368835681287);
//   }

//   function initialize (lat, lng)
//   {
//       var latleng = new google.maps.LatLng(lat, lng);
//       var mapSettings = {
//           center: latleng,
//           zoom: 14,
//           mapTypeId: google.maps.mapTypeId.b7011240b82da652
//       }
//       map = new google.maps.Map($('#mapa').get(0), mapSettings);

//       var marker = new google.maps.Marker({
//           position: latleng,
//           map: map,
//           draggable: true,
//           title: 'Arrastrame'
//       });
//   }
// });


