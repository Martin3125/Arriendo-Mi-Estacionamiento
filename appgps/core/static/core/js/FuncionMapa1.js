
    var map;
    function initMap() {
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(function (position) {
                
            const uluru = { lat: position.coords.latitude, lng: position.coords.longitude };   
            map = new google.maps.Map(document.getElementById('map'), {
                mapId: "b7011240b82da652",
                center: uluru,
                zoom: 15,
            });
        })
    }
        
      
        const listarUbicaciones = async (nombre) => {
            try {
                const response = await fetch(`./obtener`);
                const data = await response.json();
                console.log(data);
                if (data.message === "Success") {
                    let opciones = ``;

                    data.ubicaciones.forEach((ubicacion) => {

                        var marcadores = [
                            [ubicacion.nombre, ubicacion.lng, ubicacion.lat, ubicacion.disponible]

                        ];
                        // 
                        var arrendar = "arriendoEs/";
                        
                        const contentString =
                            '<div id="content">' +
                            '<div id="siteNotice">' +
                            '</div style="display: flex; text-aligm: center;">' +
                            
                            '<H5 style="color: black;">'+ ubicacion.nombre +'</H5>'+
                            
                            
                            '<a id="firstHeading" class="btn btn-info" href="'+arrendar+''+ubicacion.nombre+'">Arrendar</a>' +
                            
                            '<div id="bodyContent">' +
                            "</div>" +
                            "</div>";
                        
                        

                        
                        var infowindow = new google.maps.InfoWindow({
                            content: contentString,
                            ariaLabel: "Uluru"
                        });
                        

                            var marker, i;
                            for (i = 0; i < marcadores.length; i++) {
                                if (marcadores[i][3] == true) {
                                    marker = new google.maps.Marker({
                                        position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2], ),
                                        map: map,
                                        title: marcadores[i][0],
                                    });
                                    google.maps.event.addListener(marker, 'click', (function (marker, i) {
                                        return function () {
                                            infowindow.open(map, marker);
                                            infowindow.open({
                                            anchor: marker,
                                            map,
                                        });
                                        }
                                    })(marker, i));
                                }
                            }
                    });

                } else {
                    alert("Estacionamientos no encontrados...");
                }
            } catch (error) {
                console.log(error);
            }
        };
        const cargaInicial = async () => {
            await listarUbicaciones();
        };

        window.addEventListener("load", async () => {
            await cargaInicial();
        });

    }
   
    google.maps.event.addDomListener(window, 'load', initialize);
