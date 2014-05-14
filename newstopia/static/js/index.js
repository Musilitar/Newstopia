// JavaScript Document

$(document).ready(function() {

var container = document.querySelector('.masonry');
var msnry = new Masonry( container, {
columnWidth: 90
});

eventie.bind( container, 'click', function( event ) {
// don't proceed if item content was not clicked on
var target = event.target;
if ( !classie.has( target, 'item-content' )  ) {
return;
}
var itemElem = target.parentNode;
classie.toggleClass( itemElem, 'is-expanded' );
var paragraphElem = document.getElementsByClassName('paragraphRest');
for(var i = 0; i < paragraphElem.length; i++) {
if(jQuery(paragraphElem[i]).parents().hasClass('is-expanded')) {
classie.toggleClass( paragraphElem[i], 'is-shown' );
}
}

msnry.layout();

$("#staticSearchBar")
.stickOnScroll({
topOffset: 0,
setParentOnStick:   true,
setWidthOnStick:    true
});
$("#staticNav")
.stickOnScroll({
topOffset:          $("#staticNav").outerHeight(),
bottomOffset:       0,
setParentOnStick:   true,
setWidthOnStick:    true
});
});

$('#menuSearch').on('click', function(e) {
//voorkom refresh
e.preventDefault()
$('.container').toggleClass('clicked');
});

});