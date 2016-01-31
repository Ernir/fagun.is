
// Override for normal form behaviour
$('#mail-form').on('submit', function (event) {
    event.preventDefault();
    registerToMailingList();
});

// Main AJAX function
function registerToMailingList() {
    $.ajax({
        url: "/internals/mail-register/",
        type: "post",
        data: $("#mail-form").serialize(),

        success: function (json) {
            displaySuccess();
            console.log(json);
        },

        error: function (xhr, errmsg, err) {
            if (errmsg !== "abort") {
                alert("Something went very wrong!");
            }
        }
    });
}

function displaySuccess() {
    $("#mail-wrapper").html("<p>Takk fyrir að skrá þig á póstlista Fágunar! " +
        "Þú færð tölvupóst innan skamms til að staðfesta skráningu.</p>")
}