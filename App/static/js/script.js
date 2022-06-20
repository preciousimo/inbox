// Function to pulse the text (login page)
$(document).ready(function() {
    (function pulse() {
        $('.text-pulse').fadeOut(1000).fadeIn(1000, pulse);
    })();
});

// Function to hide/show the password
function myFunction() {
    var p = document.getElementById("password");
    if (p.type === "password") {
        p.type = "text";
    }
    else {
        p.type = "password"
    }
}