/* Google Map API initialization */

// Global variables:
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

  // if all the addresses have been geocoded and pins have been rendered on the map, recenter the map
  // with the calculated center point
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

}

// startTimer:
// runs the checkMarkers function for 10 seconds to check if the geocoding is complete to recenter the map
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

// checkMarkers:
// controls the 'hasCenter' variable which will run the initMap() function to recenter the map after flipping the boolean value
async function checkMarkers() {
  if(count >= jsonData.length && !hasCenter) {
    // console.log("Houston, we have landed");
    hasCenter = true;
    initMap();
  }
}

/* Address logic  */

// geocode:
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

// drawMarker: 
// asyncronously draw a marker on map after waiting for the geocode method to fetch data
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

  // Places API autocomplete; NOT CURRENTLY IN USE
  // var input = document.getElementById('searchLocation');
  // var autocomplete = new google.maps.places.Autocomplete(input);
}

// drawMarkers:
// utilizes Google's geocode API to determine the latitude and longitudes for each address String
function drawMarkers() {
  if(latLngList.length != jsonData.length) {
    jsonData.forEach(function (addressInfo) {
      // access each address object's formatted address field from database
      var addressString = addressInfo.address;

      // declare addressInfo to be assigned output from geocode Promise
      var addressObj;
      addressObj = geocode(addressString).then(response => {
        // console.log("result from geocode: " + response);
        // console.log("addressObj after assignment: " + addressObj);
        return response;
      }).catch(error => {
        console.log(error.message);
      });
    }) 
  }
}

// determineCenter:
// asyncronously determines the average of all the rendered pins currently on the map
async function determineCenter() {
  //console.log(latLngList);
  count = 0; // 

  // for each latLng in the list, check if it's within the bounds of Texas
  latLngList.forEach(latLngEntry => {
    if(latLngEntry.lat <= 34 && latLngEntry.lat >= 27 && latLngEntry.lng >= -106 && latLngEntry.lng <= -94) {
      //console.log(latLngEntry.lat);
      //console.log(latLngEntry.lng);
      // If so, then add one to count and to both lat/lng averages
      count++;
      latAvg += latLngEntry.lat;
      lngAvg += latLngEntry.lng;
    }
  })

  //console.log("---------");
  //console.log(latAvg);
  //console.log(lngAvg);
  //console.log(count);

  // calculate averages using the count variable
  latAvg /= count;
  lngAvg /= count;

  //console.log("output from determineCenter: ");
  //console.log("latAvg: " + latAvg + " | lngAvg:" + lngAvg);

  // return results for use in any potential callback methods
  return {
    'latAvgResult': latAvg,
    'lngAvgResult': lngAvg
  };
}

// Run these jQuery/SWAL2 functionalities once DOM has been loaded
$( document ).ready(function() {
  // Replace default HTML text in landing page select "---------"
  // with custom default 'any thing'
  $("#id_category option:first-child").text("Any Category");
  $("#id_location option:first-child").text("Any Location");

  // Used sweetalert2 to create How To pop up
  // When the HOW TO button is clicked a pop up is generated
$('#howToButton').on("click", function() {
  Swal.fire({
  // specifies the icon that appears at the top of the pop up box, question creates a question mark
  type: 'question',
  // Used p tags to create paragraphs within a single html block, <br> adds a new line
  // The + concatonates the paragraphs in the pop up, and the comma ends the html block
  // Used a video tag to embed a how to tutorial video within the html block
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
  //confirmButtonClass: 'button-text-height',
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
      if(resultLink.startsWith("www")|| !resultLink.startsWith("h")) {
        var newLink = "http://" + resultLink;
        // Change the href attribute of each link with a newly concatenated URL string
        $( this ).attr("href", newLink);        
      }
    })
  }
});



