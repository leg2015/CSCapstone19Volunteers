/* Google Map API initialization */

var map; // create global 'map' variable to be used throughout main.js
var latAvg = 0.0;
var lngAvg = 0.0;
var latLngList = [];
var count = 0;
var hasCenter = false;
var responseList = [];


// Based on this tutorial: https://developers.google.com/maps/documentation/javascript/adding-a-google-map#get_latLng
// Initialize and add the map (callback method used in maps API cdn in base.html)
async function initMap() {
  // The location of Georgetown; TODO: pass in selected location (city) to center map near results
  var centerLatLng = {
    lat: 30.6349,
    lng: -97.6651
  };

  if (hasCenter) {
    determineCenter();
    // console.log(centerLatLng);

    //console.log("Center calcualted, re-drawing map");

    // console.log(latAvg);
    // console.log(lngAvg);

    // re-render map with new center, calculated in determineCenter()
    map = new google.maps.Map(
      document.getElementById('map'), {
        zoom: 10,
        center: {
          lat: latAvg,
          lng: lngAvg
        }
      });

      responseList.forEach(function(response) {
        drawMarker(response);
      });
  } else {
  // The map, centered at given location
  // console.log("No center calculated, rendering default map");
  map = new google.maps.Map(
    document.getElementById('map'), {
      zoom: 10,
      center: centerLatLng
    });
    //var newCenter = await drawMarkers();
    drawMarkers();
    startTimer(1);
  }

  // console.log(newCenter);


  // map = new google.maps.Map(
  //   document.getElementById('map'), {
  //     zoom: 10,
  //     center: await determineCenter()
  //   });

  // while(count < jsonData.length && count != 0) {
  // }

}

function startTimer(duration) {
  var timer = duration, minutes, seconds;
  setInterval(function () {
      minutes = parseInt(timer / 60, 10)
      seconds = parseInt(timer % 60, 10);

      minutes = minutes < 10 ? "0" + minutes : minutes;
      seconds = seconds < 10 ? "0" + seconds : seconds;

      if (--timer < 0) {
          timer = duration;
      }
      checkMarkers();
  }, 1000);
}

async function checkMarkers() {
  if(count >= jsonData.length && !hasCenter) {
    // console.log("Houston, we have landed");
    hasCenter = true;
    initMap();
  }
}

// function recenterMap() {
//   console.log("recenterMap entered");

//   var markers_promise = new Promise(function(resolve, reject) {
//     // do a thing, possibly async, then…
//     // while(count < jsonData.length)
//     if (count === jsonData.length) {
//       resolve("Stuff worked!");
//     }
//     else {
//       reject(Error("It broke"));
//     }
//   });

//   console.log("promise created");

//   markers_promise.then(function(result) {
//     console.log(result); // "Stuff worked!"
//   }, function(err) {
//     console.log(err); // Error: "It broke"
//   });
// }

/* Address logic  */

// Asyncronously recieve geocoding information from API (using Axios library) with a given address string
async function geocode(addressStr) {
  await axios.get('https://maps.googleapis.com/maps/api/geocode/json?', {
    params: {
      address: addressStr,
      key: '***REMOVED***' // TODO: !!! HIDE THIS KEY BEFORE DISTRIBUTION BUILD !!!
    }
  }).then(response => {
    // log full response
    // console.log(response);
    responseList.push(response);
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

  latLngList.push({
    'lat': lat,
    'lng': lng
  });

  count++; // add one to count

  //console.log(latLngList);
  //console.log(count);

  // create a new marker 

    var marker = new google.maps.Marker({
      position: {
        lat: lat,
        lng: lng
      },
      map: map,
      title: formatted_address
    });

  // Places API autocomplete
  var input = document.getElementById('searchLocation');
  var autocomplete = new google.maps.places.Autocomplete(input);
}


function drawMarkers() {

  if(latLngList.length != jsonData.length) {
  jsonData.forEach(function (addressInfo) {
    // access each address object's formatted address field from database
    var addressString = addressInfo.address;
    // console.log(addressString);

    // declare addressInfo to be assigned output from geocode Promise
    var addressObj;
    addressObj = geocode(addressString).then(response => {
      // console.log("result from geocode: " + response);
      // console.log("addressObj after assignment: " + addressObj);
      return response;
    }).catch(error => {
      console.log(error.message);
    });

    //return determineCenter();
    // addressObj.then(result => {
    //   console.log(result);
    // });

    // var marker = new google.maps.Marker({
    //   //position: addressObj.results[0].formatted_address,
    //   position: {    lat: 30.6349,
    //     lng: -97.6651},
    //   map: map,
    //   //title: addressObj.results[0].geometry.location
    // });

    // marker.setMap(map);
  }) 
}
}

async function determineCenter() {
  //console.log(latLngList);
  count = 0;
  var outsideAreaCount = 0;

  latLngList.forEach(latLngEntry => {
    if(latLngEntry.lat <= 34 && latLngEntry.lat >= 27 && latLngEntry.lng >= -106 && latLngEntry.lng <= -94) {
      
      //console.log(latLngEntry.lat);
      //console.log(latLngEntry.lng);
      count++;
      latAvg += latLngEntry.lat;
      lngAvg += latLngEntry.lng;
    }
  })

  //console.log("---------");
  //console.log(latAvg);
  //console.log(lngAvg);
  //console.log(count);

  latAvg /= count;
  lngAvg /= count;

  //console.log("output from determineCenter: ");
  //console.log("latAvg: " + latAvg + " | lngAvg:" + lngAvg);

  return {
    'latAvgResult': latAvg,
    'lngAvgResult': lngAvg
  };
}

$( document ).ready(function() {
  // Replace default HTML text in landing page select "---------"
  // with custom default 'any thing'
  $("#id_category option:first-child").text("Any Category");
  $("#id_location option:first-child").text("Any Location");

  //console.log("method fired");

  // Use sweetalert2 to show How To message
$('#howToButton').on("click", function() {
  Swal.fire({
  type: 'question',
  html: '<h1 class="jumbotron-heading">This is your friendly how-to manual</h1><br><br>'+
  '<p>1) Click on the dropdown for category and select the category you would like to search under. <br></p>'+
  '<p>2) Click on the dropdown for location and select the location you would like to search in. <br></p>'+
  '<p>3) Click the SEARCH button. <br></p>'+
  '<p> Cards with the available opportunities will appear on the left had side of the screen and a map will appear on the right hand side of the screen showing where the opportunities are based on your search requirements, or if there are no opportunities available that match the search requirements.<br></p>'+
  '<p> To learn more about the organizations that appear in the search results, click on the Website link in the card and a new window will pop up with the website for that organization. <br></p>'+
  '<p> If you wish to contact the Office of Community-Engaged Learning, please click on the CONTACT US button at the top of the page. Thank you for visiting our page. <br></p>' +
  '<video width="450" height="300" controls> <source src="/static/images/HowToSearchVideo.mp4" type="video/mp4"> Your browser does not support the video tag. </video>' +
  '<br><br><p>Created by Colin Scruggs, Lauren Gillespie, Sara Boyd, Taylor Axtell, and Danielle Orbach as part of our senior capstone project.</p>',
  showCloseButton: true,
  confirmButtonClass: 'button-text-height',
  confirmButtonText: 'OK',
  confirmButtonColor: '#FFCD00',
  });
  })


  
  // Parse current URL
  var currentUrl = window.location.href;  

  // If user is on the results page:
  // TODO: MAKE SURE TO CHANGE URL CHECK ONCE WE'VE OBTAINED A DOMAIN NAME !!!
  if(currentUrl === "http://127.0.0.1:8000/results") {
    $( ".website_link" ).each(function(index, result) {
      var resultLink = $( this ).attr("href"); // grab each card's linked website
      // if the link is missing 'http://'
      //console.log("result link is ", resultLink);
      // HIHIHIHIH
      if(resultLink.startsWith("www")) {
        var newLink = "http://" + resultLink;
        // Change the href attribute of each link with a newly concatenated URL string
        $( this ).attr("href", newLink);        
      }
    })
  }
});



