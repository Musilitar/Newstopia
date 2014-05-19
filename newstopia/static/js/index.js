// JavaScript Document
$(document).ready(function () {

    var page = $(location).attr('href');
    var pageClean = page.split('/');

    if(pageClean[pageClean.length - 2] == "articles"){
        $('#menuHome').addClass("currentMenu");
    }else if(pageClean[pageClean.length - 3] == "articles"){
        if(pageClean[pageClean.length] - 2 == "about"){
            $('#menuAbout').addClass("currentMenu");
        }else if(pageClean[pageClean.length - 3] == "archive"){
            $('#menuArchive').addClass("currentMenu");
        }else if(pageClean[pageClean.length - 3] == "create"){
            $('#menuNewArticle').addClass("currentMenu");
        }
    }else{
        $('#ProfileIcon').addClass("currentMenu");
    }


    var container = document.querySelector('.masonry');
    if(container){
        var msnry = new Masonry(container, {
        columnWidth: 90
        });
    }

    if($('.btnRead')){
        $('.btnRead').click(function(event){
            var target;

            if($(event.target).hasClass("btnRead")){
                target = event.target;
            }else {
                target = event.target.parent();
                alert("notbtnRead");
            }
            var itemElem = target.parentNode.parentNode.parentNode.parentNode;
            classie.toggleClass(itemElem, 'is-expanded');

            //set text margin
            if (jQuery(target).parent().parent().parent().parent().hasClass('is-expanded')){
                jQuery(target).parent().parent().parent().css( 'height', '95%');
            } else {
                if(jQuery(target).parent().parent().parent().hasClass('item-content-big')) {
                    //jQuery(target).parent().parent().parent().css( 'height', '95%')
                }
                else {
                    jQuery(target).parent().parent().parent().css( 'height', '265px');
                }
            }

            //load new paragraphs
            if (jQuery(target).parent().parent().parent().children('.paragraphRest').css('display') == 'none') {
                jQuery(target).parent().parent().parent().children('.paragraphRest').css('display', 'block');
            } else {
                jQuery(target).parent().parent().parent().children('.paragraphRest').css("display", "none");
            }

            //change more button
            if (jQuery(target).parent().parent().parent().parent().hasClass('is-expanded')){
            $(target).html('<i class="fa fa-arrow-circle-up"></i> less');
            } else {
            $(target).html('<i class="fa fa-arrow-circle-down"></i> more');
            }

            msnry.layout();
            $(window).resize();
        });
    }

    //submit Login
    $("#submitLogin").click(function (event) {
        $("form[name='login']").submit();
    });

});