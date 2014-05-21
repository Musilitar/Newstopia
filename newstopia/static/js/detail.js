$(document).ready(function() {

//submit new paragraph
    $("#submitBtn").click(function (event) {
      $("form[name='newParagraph']").submit();
    });

    $('#paragraphText').keydown(function (e){
        if(e.keyCode == 13){
            $("form[name='newParagraph']").submit();
        }
    });
});