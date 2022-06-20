// Function to pulse the text (login page)
$(document).ready(function() {
    (function pulse() {
        $('.text-pulse').fadeOut(1000).fadeIn(1000, pulse);
    })();
});
