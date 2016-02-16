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
            displaySuccess(json);
        },

        error: function (xhr, errmsg, err) {
            if (errmsg !== "abort") {
                // ToDo: Handle this type of error
            }
        }
    });
}

function displaySuccess(json) {
    $("#mail-wrapper").html(json.response)
}