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

$( document ).ready(function() {
  // Replace default HTML text in landing page select "---------"
  // with custom default 'any thing'
  $("#id_category option:first-child").text("Any Category");
  $("#id_location option:first-child").text("Any Location");
  console.log("method fired");

  // Use sweetalert2 to show About message
$('#aboutButton').on("click", function() {
  Swal.fire({
  type: 'question',
  html: '<h1 class="jumbotron-heading">This is your friendly how-to manual</h1><br><br>'+
  '<p>1) Click on the dropdown for category and select the category you would like to search under. <br><br></p>'+
  '<p>2) Click on the dropdown for location and select the location you would like to search in. <br><br></p>'+
  '<p>3) Click the SEARCH button.<br><br></p>' +
  // discuss what the results will desplay like and remember to mention how the maps will render (ask Colin)
  '<p> Cards with the available opportunities will appear on the left had side of the screen and a map will appear on the right hand side of the screen showing where the opportunities are in relation to you based on your search requirements, or if there are no opportunities available that match the search requirements. <br><br></p>'+
  '<p> If you wish to learn more about the organizations that appear in the search results, click on the "Website" link in the card and a new window will pop up with the website for that organization. Thank you for visiting our page. <br><br></p>',
  showCloseButton: true,
  showCancelButton: true,
  cancelButtonClass: 'button-text-height',
  confirmButtonClass: 'button-text-height',
  cancelButtonColor: '#FFCD00',
  confirmButtonText: 'OK',
  confirmButtonColor: '#6c757d',
  cancelButtonText: 'Refine Search',
  }
  ).then((value) => {
  if(value.dismiss == 'cancel'){
  Swal.fire({
  type: 'question',
  html: '<h1 class="jumbotron-heading">How to refine your search</h1><br><br>' +
  '<p>1) Click on the dropdown for category and select the category you would like to search under. <br><br></p>'+
  '<p>2) Type in the city or address of location you are searching from. <br><br></p>'+
  '<p>3) Enter a search radius in miles for how far you wish to travel from your starting location. <br><br></p>' +
  '<p>4) Click the SEARCH button.</p>',
  confirmButtonColor: '#FFCD00',
  showCloseButton: true,
  });
  }
  });
  })
  });