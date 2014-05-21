$(document).ready(function () {

    $('#menuSearch').on('click', function (e) {
        //voorkom refresh
        e.preventDefault()
        if($('#staticLoginBar').hasClass('clicked')){
            $('#staticLoginBar').toggleClass('clicked');
        }
        $('.container').toggleClass('clicked');
        $('#staticSearchBar').toggleClass('clicked');

        //checken of het menu bovenaan staat
        var distance = $('#staticNav').offset().top,
            $window = $(window);
        if ($window.scrollTop() >= distance) {
            $('#staticNav').toggleClass('clicked');
        }
    });

    $('#menuProfile').on('click', function (e) {
        //voorkom refresh
        e.preventDefault()
        if($('#staticSearchBar').hasClass('clicked')){
            $('#staticSearchBar').toggleClass('clicked');
        }

        $('.container').toggleClass('clickedProfile');
        $('#staticLoginBar').toggleClass('clicked');
        if( $(".first-link:contains('profile')").length > 0) {
            $(location).attr('href', '/account/');
        }

        //checken of het menu bovenaan staat
        var distance = $('#staticNav').offset().top,
            $window = $(window);
        if ($window.scrollTop() >= distance) {
            $('#staticLoginBar').toggleClass('clicked');
        }
    });

    $("#staticSearchBar")
        .stickOnScroll({
            topOffset: 0,
            setParentOnStick: true,
            setWidthOnStick: true
        });

    $("#staticLoginBar")
        .stickOnScroll({
            topOffset: 0,
            setParentOnStick: true,
            setWidthOnStick: true
        });

    $("#staticNav")
        .stickOnScroll({
            topOffset: 0,
            bottomOffset: 0,
            setParentOnStick: true,
            setWidthOnStick: true
        });

});