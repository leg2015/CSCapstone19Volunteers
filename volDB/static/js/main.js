// Based on this tutorial: https://developers.google.com/maps/documentation/javascript/adding-a-google-map#get_latLng
// Initialize and add the map
function initMap() {
  // The location of Uluru
  var georgetown = {
    lat: 30.6349,
    lng: -97.6651
  };
  // The map, centered at Uluru
  var map = new google.maps.Map(
    document.getElementById('map'), {
      zoom: 10,
      center: georgetown
    });
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({
    position: georgetown,
    map: map
  });
}

/* Landing page form replacement */

$( document ).ready(function() {
  // Replace default HTML text in landing page select "---------"
  // with custom default 'any thing'
  $("#id_category option:first-child").text("Any Category");
  $("#id_location option:first-child").text("Any Location");
});

/* Address logic  */

var jsonData = [];

// Grab data from serialized json object (passed in base.html) 
function jsonPass(data){
  data.forEach(function(address) {
    jsonData.push({'orgId':address.fields.orgID, 'fields':address.fields,
                   'address': address.fields.street + ', ' + address.fields.city + ', ' + 
                              address.fields.state + ' ' + address.fields.zipCode})
  })
  console.log(jsonData);

  return data;
}

jsonData.forEach(function(addressObj) {
  var addressString = addressObj.address;
  //var geocode = https://maps.googleapis.com/maps/api/geocode/json?address=addressString&key=***REMOVED***;
  var marker = new google.maps.Marker({
    position: georgetown,
    title:addressObj.address
  });
  console.log(geocode);
})