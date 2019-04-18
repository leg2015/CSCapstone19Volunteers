
/* Landing page form replacement */

$( document ).ready(function() {
  // Replace default HTML text in landing page select "---------"
  // with custom default 'any thing'
  $("#id_category option:first-child").text("Any Category");
  $("#id_location option:first-child").text("Any Location");
});

/* Google Map API initialization */

var map; // create global 'map' variable to be used throughout main.js

// Based on this tutorial: https://developers.google.com/maps/documentation/javascript/adding-a-google-map#get_latLng
// Initialize and add the map (callback method used in maps API cdn in base.html)
async function initMap() {
  // The location of Georgetown; TODO: pass in selected location (city) to center map near results
  var georgetown = {
    lat: 30.6349,
    lng: -97.6651
  };
  // The map, centered at given location
  map = new google.maps.Map(
    document.getElementById('map'), {
      zoom: 10,
      center: georgetown
    });

   await drawMarkers();
}

/* Address logic  */

// Asyncronously recieve geocoding information from API (using Axios library) with a given address string
async function geocode(addressStr) {
  await axios.get('https://maps.googleapis.com/maps/api/geocode/json?', {
    params: {
      address: addressStr,
      key:'***REMOVED***' // TODO: !!! HIDE THIS KEY BEFORE DISTRIBUTION BUILD !!!
    }
  }).then(response => {
    // log full response
    // console.log(response);
    drawMarker(response);
    // TODO: pass organization name along with json data for adding labels to markers

    return response;
  }).catch(error => {
    console.log("Google Maps Geocoding API error: " + error);
  })
}

// drawMarker: asyncronously draw a marker on map after waiting for the geocode method to fetch data
async function drawMarker(response) {
  // console.log("output from drawMarker function:");
  // console.log(response);

  // grab latitude and longitude 
  var lat = response.data.results[0].geometry.location.lat;
  var lng = response.data.results[0].geometry.location.lng;
  var formatted_address = response.data.results[0].formatted_address;
  // console.log("Rendering pin at latitude: " + lat + " | longitude: " + lng);

  // create a new marker 
  var marker = new google.maps.Marker({
    
    position: { lat: lat, lng: lng},
    map: map,
    title: formatted_address
  });
}

// old attempt: keeping for one commit (TODO: delete this before next commit)
// function drawMarkers() {

//   jsonData.forEach(function(addressInfo) {
//     // access each address object's formatted address field from database
//     var addressString = addressInfo.address;
//     // console.log(addressString);
    
//     // declare addressInfo to be assigned output from geocode Promise
//     var addressObj;
//     addressObj = geocode(addressString).then(response => {
//       console.log("result from geocode: " + response);
//       // console.log("addressObj after assignment: " + addressObj);
//       return response;
//       response.json({ message: 'Request recieved in drawmMarkers!', data})
//       console.log(response.json({ message: 'Request recieved in drawmMarkers!', data}));
//       addressObj = result;
//       console.log("result from geocode: " + result);
//       console.log("addressObj after assignment: " + addressObj);
//     }).catch(error => {
//       console.log(error.message);
//     });

//     addressObj.then(result => {
//       console.log(result);
//     });

//     var marker = new google.maps.Marker({
//       //position: addressObj.results[0].formatted_address,
//       position: {    lat: 30.6349,
//         lng: -97.6651},
//       map: map,
//       //title: addressObj.results[0].geometry.location
//     });

//     marker.setMap(map);
//   })
// }