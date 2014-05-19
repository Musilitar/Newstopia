/**
 * Created by MalefD on 17/05/14.
 */
$(document).ready(function(){
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        if($('.btnUp')){

            $('.btnUp').click(function(){
                ref = $(this);
                article = $(this).parent().parent().children()[2].href;
                article = article.split("/");
                articlenumber = parseInt(article[article.length - 2]);
                $.post('/articles/vote/', {id: articlenumber, type: "article", difference: 1}, function(data){
                    thisButton = ref;
                    otherButton = ref.parent().children()[1];
                    score = ref.parent().children()[2].innerHTML;
                    var intscore = parseInt(score);
                    intscore++;
                    ref.parent().children()[2].innerHTML = "" + intscore.toString();
                    thisButton.remove();
                    otherButton.remove();

                });
            });
        }

        if($('.btnDown')){
            $('.btnDown').click(function(){
                ref = $(this);
                article = $(this).parent().parent().children()[2].href;
                article = article.split("/");
                articlenumber = parseInt(article[article.length - 2]);
                $.post('/articles/vote/', {id: articlenumber, type: "article", difference: -1}, function(data){
                    thisButton = ref;
                    otherButton = ref.parent().children()[0];
                    score = ref.parent().children()[2].innerHTML;
                    var intscore = parseInt(score);
                    intscore--;
                    ref.parent().children()[2].innerHTML = "" + intscore.toString();
                    thisButton.remove();
                    otherButton.remove();
                });
            });
        }

        if($('.pbtnUp')){

            $('.pbtnUp').click(function(){
                ref = $(this);
                article = $(this).parent().parent().parent().children()[0].id;
                articlenumber = parseInt(article);
                $.post('/articles/vote/', {id: articlenumber, type: "paragraph", difference: 1}, function(data){
                    thisButton = ref;
                    otherButton = ref.parent().children()[2];
                    score = ref.parent().children()[1].innerHTML;
                    var intscore = parseInt(score);
                    intscore++;
                    ref.parent().children()[1].innerHTML = "" + intscore.toString();
                    thisButton.remove();
                    otherButton.remove();

                });
            });
        }

        if($('.pbtnDown')){
            $('.pbtnDown').click(function(){
                ref = $(this);
                article = $(this).parent().parent().parent().children()[0].id;
                articlenumber = parseInt(article);
                $.post('/articles/vote/', {id: articlenumber, type: "paragraph", difference: -1}, function(data){
                    thisButton = ref;
                    otherButton = ref.parent().children()[0];
                    score = ref.parent().children()[1].innerHTML;
                    var intscore = parseInt(score);
                    intscore--;
                    ref.parent().children()[1].innerHTML = "" + intscore.toString();
                    thisButton.remove();
                    otherButton.remove();
                });
            });
        }
    }
);