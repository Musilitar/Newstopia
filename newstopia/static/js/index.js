// JavaScript Document

    var container = document.querySelector('.masonry');
    var msnry = new Masonry(container, {
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
    if(jQuery(target).children('.paragraphRest').css('display') == 'none') {
        jQuery(target).children('.paragraphRest').css('display', 'inline');
    }
    else {
        jQuery(target).children('.paragraphRest').css("display", "none");
    }
    msnry.layout();
  });
});