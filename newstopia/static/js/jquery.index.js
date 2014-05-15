$(document).ready(function () {

    $('#menuSearch').on('click', function (e) {
        //voorkom refresh
        e.preventDefault()
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
        $('.container').toggleClass('clicked');
        $('#staticLoginBar').toggleClass('clicked');

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

    $("#staticNav")
        .stickOnScroll({
            topOffset: 0,
            bottomOffset: 0,
            setParentOnStick: true,
            setWidthOnStick: true
        });

});