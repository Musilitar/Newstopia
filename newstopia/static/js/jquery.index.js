$(document).ready(function () {

    $('#menuSearch').on('click', function (e) {
        //voorkom refresh
        e.preventDefault()
        $('.container').toggleClass('clicked');
        $('#staticSearchBar').toggleClass('clicked');

        //if nog juist zetten maar deze methode gebruiken
        var distance = $('#staticNav').offset().top,
            $window = $(window);
        if ($window.scrollTop() >= distance) {
            $('#staticNav').toggleClass('clicked');
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