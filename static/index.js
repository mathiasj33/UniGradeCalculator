$(document).ready(function () {
    $("#signInBtn").click(function () {
        $(".fade-out").fadeOut(500, function() {
            $(".login-form").fadeIn(500);
        });
    });
});
