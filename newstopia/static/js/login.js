$(document).ready(function() {
    $("#submitLogin").click(function (event) {
        $("form[name='login']").submit();
    });

    $('#passwordField').keydown(function (e){
        if(e.keyCode == 13){
            $("form[name='login']").submit();
        }
    });
});