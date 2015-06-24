function setHeroHeight() { 
    // Set height of hero
    var windowHeight = $(window).height();
    var headerHeight = $('header').height();

    $('#hero').height(windowHeight - headerHeight);
}

$(document).ready(function() {
    setHeroHeight();
});
