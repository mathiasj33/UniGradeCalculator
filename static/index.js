$(document).ready(function () {
    $("#signin-btn").click(function () {
        $(".fade-out").fadeOut(500, function () {
            $(".login-form").fadeIn(500);
        });
    });

    $("#back-btn").click(function () {
        $(".login-form").fadeOut(500, function () {
            $(".fade-out").fadeIn(500);
        });
        $("#error-text").fadeOut(500);
    });

    $("#login-button").click(login);
    $("#password").keypress(function (e) {
        if (e.which == 13) {
            login();
        }
    });
});

function login() {
    $("#error-text").fadeOut();
    $.post("/login", {
        username: $("#username").val(),
        password: $("#password").val()
    }, function (response) {
        if (response == "ok") {
            window.location.replace("/dashboard")
        }
        else {
            $("#error-text").fadeIn();
        }
    });
}
