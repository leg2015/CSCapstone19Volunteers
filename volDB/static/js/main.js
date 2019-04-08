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
  //   // Use sweetalert2 to show About message
  //   Swal.fire({
  //     // title: ‘<span id=“title”>About SU Radio</span>‘,
  //     // showCloseButton: true,
  //     // focusConfirm: false,
  //     // html: `<p style=“font-family: Roboto”>SU Radio is the independent, student run online radio station of Southwestern University. <br>
  //     //         Student’s talk shows, podcasts, and DJ sets are broadcasted here every week. Interested in joining? <br>
  //     //         <strong>Contact southwesternuradio@gmail.com</strong>
  //     //         <br> <br>
  //     //         This site was built as a part of SU’s King Creativity grant in 2019.
  //     //       </p>`,
  //     // confirmButtonText: ‘<span style=“font-family: Roboto;“>OK</span>‘,
  //     // confirmButtonColor: ‘#FFD54F’
  //   });console.log("method fired");
//   // Use sweetalert2 to show About message
//   Swal.fire({
//     // title: ‘<span id=“title”>About SU Radio</span>‘,
//     // showCloseButton: true,
//     // focusConfirm: false,
//     // html: `<p style=“font-family: Roboto”>SU Radio is the independent, student run online radio station of Southwestern University. <br>
//     //         Student’s talk shows, podcasts, and DJ sets are broadcasted here every week. Interested in joining? <br>
//     //         <strong>Contact southwesternuradio@gmail.com</strong>
//     //         <br> <br>
//     //         This site was built as a part of SU’s King Creativity grant in 2019.
//     //       </p>`,
//     // confirmButtonText: ‘<span style=“font-family: Roboto;“>OK</span>‘,
//     // confirmButtonColor: ‘#FFD54F’
//   });
$('#aboutButton').on("click", function() {
  // console.log("method fired");
  // Use sweetalert2 to show About message
  Swal.fire({
  type: 'question',
  html: '<h1 class="jumbotron-heading">This is your friendly how-to manual</h1><br><br>'+
  '<p>1) Click on the dropdown for category and select the category you would like to search under. <br><br></p>'+
  '<p>2) Click on the dropdown for location and select the location you would like to search in. <br><br></p>'+
  '<p>3) Click the SEARCH button.</p>',
  // discuss what the results will desplay like and remember to mention how the maps will render (ask Colin)
  showCloseButton: true,
  showCancelButton: true,
  cancelButtonColor: '#FFCD00',
  confirmButtonText: 'OK',
  confirmButtonColor: '#6c757d',
  cancelButtonText: 'Refine Search',
  }
  ).then((value) => {
  console.log(value.dismiss != 'cancel');
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
  console.log("method fired");
  });
  })
  });