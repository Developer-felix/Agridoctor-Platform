(function($){
  $(function(){
    $('.tabs').tabs();
    $('.sidenav').sidenav();
    $('.slider').slider({
      fullWidth: true,
      indicators: false,
      height: 500
    });
    $('.carousel').carousel();
    $('.materialboxed').materialbox();
    $('.modal-trigger').leanModal();
    $(".button-collapse").sideNav();

    $('.modal').modal();
    $('#modal1').openModal();
    $(window).scroll(function(){
      if($(window).scrollTop()>300){
        $('nav').addClass('red');
      }else{
        $('nav').removeClass('red');
      }
    })

    }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function(){
  $(".button-collapse").sideNav();
})
