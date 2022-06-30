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

// Character remaining counter
$(document).ready(function() {
    var start = 0;
    var limit = 1000;

    $('#message').keyup(function() {
        start = this.value.length
        if (start > limit) {
            return false;
        }
        else if (start == 1000) {
            $("#remaining").html("Characters remaining: " + (limit - start)).css('color', 'red');
            swal("Oops!!", "Characters limit exceeded !", "info");
        }
        else if (start > 984) {
            $("#remaining").html("Characters remaining: " + (limit - start)).css('color', 'red');
        }
        else if (start < 1000) {
            $("#remaining").html("Characters remaining: " + (limit - start)).css('color', 'black');
        }
        else {
            $("#remaining").html("Characters remaining: " + (limit)).css('color', 'black');
        }
    })
});

// Inputmask (PHONE)
$(document).ready(function() {
    $(".phone").inputmask("9999-999-9999", {"onincomplete": function() {
        swal("Opss !", "Incomplete phone. Please review !", "Info");
        $(".phone").val("");
        return false; 
    }})
})

// Script to accept until 2mb 'upload file'
$(document).ready(function() {
    var upload = document.getElementById('file');
    upload.onchange = function() {
        if(this.files[0].size > 2 * 1048576) {
            swal("Attention !", "Maximum allowed size is 2mb.", "info");
            this.value = "";
        };
    };
});