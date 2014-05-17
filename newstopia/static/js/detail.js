$(document).ready(function() {

  var container = document.querySelector('.masonry');
  if(container){
      var msnry = new Masonry( container, {
        columnWidth: 180
      });
  }
});