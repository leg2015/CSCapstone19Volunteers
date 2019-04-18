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
  // Places API autocomplete
  var input = document.getElementById('searchLocation');
  var autocomplete = new google.maps.places.Autocomplete(input);
}


$( document ).ready(function() {
  // Replace default HTML text in landing page select "---------"
  // with custom default 'any thing'
  $("#id_category option:first-child").text("Any Category");
  $("#id_location option:first-child").text("Any Location");

  
  // Parse current URL
  var currentUrl = window.location.href;  

  // If user is on the results page:
  // TODO: MAKE SURE TO CHANGE URL CHECK ONCE WE'VE OBTAINED A DOMAIN NAME !!!
  if(currentUrl === "http://127.0.0.1:8000/results") {
    $( ".website_link" ).each(function(index, result) {
      var resultLink = $( this ).attr("href"); // grab each card's linked website
      // if the link is missing 'http://'
      console.log("result link is ", resultLink);
      // HIHIHIHIH
      if(resultLink.startsWith("www")) {
        var newLink = "http://" + resultLink;
        // Change the href attribute of each link with a newly concatenated URL string
        $( this ).attr("href", newLink);        
      }
    })
  }

});