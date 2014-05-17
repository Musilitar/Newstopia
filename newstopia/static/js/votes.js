/**
 * Created by MalefD on 17/05/14.
 */
$(document).ready(function(){
        if($('.btnUp')){

            $('.btnUp').click(function(event){
                $.post('/articles/vote', {}, function(data){

                });
            });
        }
    }
);