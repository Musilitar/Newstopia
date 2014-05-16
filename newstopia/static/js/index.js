// JavaScript Document
$(document).ready(function () {

    var container = document.querySelector('.masonry');
    var msnry = new Masonry(container, {
        columnWidth: 90
    });

    $(btnRead).click(function(event){
        alert("klik");
        var target = event.target;
        var itemElem = target.parentNode.parentNode.parentNode.parentNode;
        classie.toggleClass(itemElem, 'is-expanded');

        if (jQuery(target).parent().parent().parent().children('.paragraphRest').css('display') == 'none') {
            jQuery(target).parent().parent().parent().children('.paragraphRest').css('display', 'block');
        } else {
            jQuery(target).parent().parent().parent().children('.paragraphRest').css("display", "none");
        }
        msnry.layout();
    });
});