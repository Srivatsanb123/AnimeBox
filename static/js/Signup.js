function validateForm() {
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("pwd").value;
    var confirm_password = document.getElementById("cpwd").value;

    if (username == "") {
        alert("Please enter your username.");
        return false;
    }
    if (email == "") {
        alert("Please enter your email.");
        return false;
    }
    if (password == "") {
        alert("Please enter your password.");
        return false;
    }
    if (confirm_password == "") {
        alert("Please confirm your password.");
        return false;
    }
    if (password != confirm_password) {
        alert("Passwords do not match.");
        return false;
    }
    return true;
}

var form = document.querySelector("form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (validateForm()) {
        form.submit();
    }
});
