///////////////
//javaScript for Posts page
///////////////////

$(function() {
    // Expected when js-menu-icon js cliked
   $('.js-menu-icon').click(function(){
    //$(this) : Self element, namely div.js-menu-icon
    //next() : Next to div.js.js-menu-icon, namely div,menu
    //toggle() : Switch show and hide  
    $(this).next().toggle();
   })
})