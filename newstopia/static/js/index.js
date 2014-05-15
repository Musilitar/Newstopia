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
        if(target.children()[4].css("display") == 'none'){
            target.children().css('display:inline');
        }else{
            target.children().slice(2, 5).css('display:none');
        }

        msnry.layout();

    });
});