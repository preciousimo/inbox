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

// Script to close the offcanvas when the button id clicked
$(document).ready(function() {
    jQuery("#offcanvasRight, .offcanvas-body a").click(function() {
        console.log($(this).attr('href'));
        jQuery('.offcanvas').offcanvas('hide');
    });
});

// If no message, hide all content
$(document).ready(function() {
    var verify = $('#chk_td').length;
    if (verify == 0) {
        $(".hidee").css('display', 'none');
        $('#msg').text("No message found!");
        $('#refresh').html('<i class="fas fa-sync-alt fa-3x">')
    }
});

// Script to get TIME running at real time
setInterval(function() {
    var date = new Date();
    $('#clock, #mini-clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" +
        (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" +
        (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);

// Script to update the page always at (0:00)
function autoRefresh(h, m, s) {
    var now = new Date(), then = new Date();
    then.setHours(h,m,s,0);
    if (then.getTime() < now.getTime()) {
        then.setDate(now.getDate() + 1);
    }
    var timeout = (then.getTime() - now.getTime());
    setTimeout(function() {
        window.location.reload(true);
    }, timeout);
}
autoRefresh(0,0,0)