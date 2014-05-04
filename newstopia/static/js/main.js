// JavaScript Document

$(document).ready(function() {
    var months = [
    'Januari', 'Februari', 'Maart', 'April', 'Mei', 'Juni', 'Juli',
    'Augustus', 'September', 'Oktober', 'November', 'December'
    ];
    var today = new Date();
    document.getElementById('date').innerHTML = today.getDate() + " " + months[today.getMonth()] + " " + today.getFullYear();
});


$(document).ready(function() {

  var container = document.querySelector('.masonry');
  var msnry = new Masonry( container, {
    columnWidth: 60
  });

  eventie.bind( container, 'click', function( event ) {
    // don't proceed if item content was not clicked on
    var target = event.target;
    if ( !classie.has( target, 'item-content' )  ) {
      return;
    }
    var itemElem = target.parentNode;
    classie.toggleClass( itemElem, 'is-expanded' );

    msnry.layout();
    console.log("clicked upon");
  });

});