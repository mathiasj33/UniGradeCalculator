$(document).ready(function () {
    $("#signin-btn").click(function () {
        $(".fade-out").fadeOut(500, function() {
            $(".login-form").fadeIn(500);
        });
    });

    $("#back-btn").click(function() {
        $(".login-form").fadeOut(500, function() {
            $(".fade-out").fadeIn(500);
        });
    });
});
