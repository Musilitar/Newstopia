$(document).ready(function() {

    $("#submitBtn").click(function (event) {
        $("form[name='newArticle']").submit();
    });

    $('#inputTags').keydown(function (e){
        if(e.keyCode == 13){
            $("form[name='newArticle']").submit();
        }
    });
});