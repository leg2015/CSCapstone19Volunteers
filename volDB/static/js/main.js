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
  console.log("method fired");
//   // Use sweetalert2 to show About message
  Swal.fire(
    "This is your friendly how-to manual."
    // "1.) Click on the dropdown for category and select the category you would like to search under."
    // "2.) Click on the dropdown for location and select the location you would like to search in."
    // "3.) Click the SEARCH button."
  );
})

});
