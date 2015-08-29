// FitText.js
(function($){
  $.fn.fitText = function( kompressor, options ) {
    // Setup options
    var compressor = kompressor || 1,
        settings = $.extend({
          'minFontSize' : Number.NEGATIVE_INFINITY,
          'maxFontSize' : Number.POSITIVE_INFINITY
        }, options);
    return this.each(function(){

      // Store the object
      var $this = $(this);

      // Resizer() resizes items based on the object width divided by the compressor * 10
      var resizer = function () {
        $this.css('font-size', Math.max(Math.min($this.width() / (compressor*10), parseFloat(settings.maxFontSize)), parseFloat(settings.minFontSize)));
      };

      // Call once to set.
      resizer();

      // Call on resize. Opera debounces their resize by default.
      $(window).on('resize.fittext orientationchange.fittext', resizer);
    });
  };
})(jQuery);

// Helpers
function isSafari() {
  return /^((?!chrome).)*safari/i.test(navigator.userAgent);
}

function validateContactForm() {
  if ($('#write #name').val() === '' || $('#write #email').val() === '' || $('#write #subject').val() === '' || $('#write #message').val() === '') {
    alert('Please fill in the details in the form!');
    return false;
  }
  emailIsSending();
  return true;
}

function emailIsSending() {
  var message = "<div id='messages-container' class='is-open'> <script>var TIMEOUT=3000; var $messages=$('#messages-container'); console.log($messages); if ($messages !==''){ setTimeout(function(){$messages.toggleClass('is-open');}, TIMEOUT);}</script> <div class='message'> <span class='content'>Your email has been sent. We will get back to you shortly!</span> </div></div>";

  $(document.body).append(message);
}

function setHeroHeight() {
    var windowHeight = $(window).height();
    var headerHeight = $('header').height();

    $('#hero').height(windowHeight - headerHeight);
}

$(document).ready(function() {
    // Set height of hero
    setHeroHeight();

    // FitText for upcoming events section
    $('#upcoming-event .content h1').fitText();
    $('#upcoming-event .content h2').fitText({ maxFontSize: '5em' });

    // Tweaks for safari
    if (isSafari()) {
      $('#hero #arrow svg').css({
        'width': '100%',
        'height': '18px'
      });
    }
});
