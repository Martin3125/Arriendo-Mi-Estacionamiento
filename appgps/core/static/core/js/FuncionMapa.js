
    // var map;
    // function initMap() {

    //     const uluru = { lat: -33.69417055239359, lng: -71.21368835681287 };
    //     map = new google.maps.Map(document.getElementById('map'), {
    //         mapId: "b7011240b82da652",
    //         center: uluru,
    //         zoom: 15,

    //     });




    //     let mark = [];
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
    //                             title: "Uluru (Ayers Rock)",
    //                         });
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
    //     const cargaInicial = async () => {
    //         await listarUbicaciones();
    //     };

    //     window.addEventListener("load", async () => {
    //         await cargaInicial();
    //     });

    //     const contentString =
    //     '<div id="content">' +
    //     '<div id="siteNotice">' +
    //     "</div>" +
    //     '<h1 id="firstHeading" class="firstHeading">Uluru</h1>' +
    //     '<div id="bodyContent">' +
    //     "<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large " +
    //     "sandstone rock formation in the southern part of the " +
    //     "Northern Territory, central Australia. It lies 335&#160;km (208&#160;mi) " +
    //     "south west of the nearest large town, Alice Springs; 450&#160;km " +
    //     "(280&#160;mi) by road. Kata Tjuta and Uluru are the two major " +
    //     "features of the Uluru - Kata Tjuta National Park. Uluru is " +
    //     "sacred to the Pitjantjatjara and Yankunytjatjara, the " +
    //     "Aboriginal people of the area. It has many springs, waterholes, " +
    //     "rock caves and ancient paintings. Uluru is listed as a World " +
    //     "Heritage Site.</p>" +
    //     '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">' +
    //     "https://en.wikipedia.org/w/index.php?title=Uluru</a> " +
    //     "(last visited June 22, 2009).</p>" +
    //     "</div>" +
    //     "</div>";
        
    //     var infowindow = new google.maps.InfoWindow();
    //     var marker, i;
    //     for (i = 0; i < marcadores.length; i++) {
    //         marker = new google.maps.Marker({
    //             position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2]),
    //             map: map
    //         });
    //         google.maps.event.addListener(marker, 'click', (function (marker, i) {
    //             return function () {
    //                 var html = "<button></button>";
    //                 var infoWindow = new google.maps.InfoWindow({content: html});
    //                 infowindow.setContent(marcadores[i][0]);
    //                 infowindow.open(map, marker);
    //             }
    //         })(marker, i));

    //     }
    // }
    // google.maps.event.addDomListener(window, 'load', initialize);



    var map;
    function initMap() {
        const uluru = { lat: -33.69417055239359, lng: -71.21368835681287 };
        map = new google.maps.Map(document.getElementById('map'), {
            mapId: "b7011240b82da652",
            center: uluru,
            zoom: 15,

        });
        // data.ubicaciones.forEach((ubicacion) => {
        //     // var marcadores += [[]];



        // });



        let mark = [];
        const listarUbicaciones = async (nombre) => {
            try {
                const response = await fetch(`./obtener`);
                const data = await response.json();
                console.log(data);
                if (data.message === "Success") {
                    let opciones = ``;

                    data.ubicaciones.forEach((ubicacion) => {

                        var marcadores = [
                            [ubicacion.nombre, ubicacion.lng, ubicacion.lat]

                        ];
                        const contentString =
                            '<div id="content">' +
                            '<div id="siteNotice">' +
                            "</div>" +
                            '<a id="firstHeading" class="btn btn-info">Arrendar</a>' +
                            '<div id="bodyContent">' +
                            "</div>" +
                            "</div>";
                        
                        

                        
                        var infowindow = new google.maps.InfoWindow({
                            content: contentString,
                            ariaLabel: "Uluru"
                        });
                            
                        var marker, i;
                        for (i = 0; i < marcadores.length; i++) {
                            marker = new google.maps.Marker({
                                position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2]),
                                map: map,
                                title: "Uluru (Ayers Rock)",
                            });
                            google.maps.event.addListener(marker, 'click', (function (marker, i) {
                                return function () {
                                    // infowindow.setContent(marcadores[i][0]);
                                    infowindow.open(map, marker);
                                    infowindow.open({
                                    anchor: marker,
                                    map,
                                });
                                }
                            })(marker, i));
                        }
                    });
                    cboUbicacion.innerHTML = opciones;

                } else {
                    alert("Países no encontrados...");
                }
            } catch (error) {
                console.log(error);
            }
        };
        const cargaInicial = async () => {
            await listarUbicaciones();

            // cboUbicacion.addEventListener("change", (event) => {
            //     mostrarUbicacion(event.target.value);
            // });
        };

        window.addEventListener("load", async () => {
            await cargaInicial();
        });

        var infowindow = new google.maps.InfoWindow();
        var marker, i;
        for (i = 0; i < marcadores.length; i++) {
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2]),
                map: map
            });
            google.maps.event.addListener(marker, 'click', (function (marker, i) {
                return function () {
                    var html = "<button></button>";
                    var infoWindow = new google.maps.InfoWindow({content: html});
                    infowindow.open(map, marker);
                }
            })(marker, i));
        }
    }
   
    google.maps.event.addDomListener(window, 'load', initialize);
