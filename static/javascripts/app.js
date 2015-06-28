function setHeroHeight() { 
    var windowHeight = $(window).height();
    var headerHeight = $('header').height();

    $('#hero').height(windowHeight - headerHeight);
}

$(document).ready(function() {
    // Set height of hero
    setHeroHeight();

    // Arrow click listener
    $('#arrow').on('click', function() {
        $('html, body').animate({
            scrollTop: $("#about").offset().top
        }, 900);
        $(this).fadeOut("slow");
    });
});
