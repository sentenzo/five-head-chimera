"use strict";

(function () {

    const backend_handler_url = "http://localhost:9999/feedback"
    // "https://httpbin.org/put";

    const btn_submit = document.getElementById("btn_submit");
    btn_submit.onclick = function (event) {
        event.preventDefault();

        let feedback = {};
        feedback.sender = {};
        feedback.sender.last_name = document.getElementById("last_name").value;
        feedback.sender.first_name = document.getElementById("first_name").value;
        feedback.sender.patronym = document.getElementById("patronym").value;
        feedback.sender.phone = document.getElementById("phone").value;
        feedback.message = document.getElementById("feedback_text").value;
        console.log(JSON.stringify(feedback, null, 2));

        // https://stackoverflow.com/a/47065313/2493536
        fetch(backend_handler_url, {
            method: "PUT",
            headers: {
                'Access-Control-Request-Method': 'PUT',
                'Access-Control-Request-Headers': 'Content-Type',
                'Origin': 'http://localhost:8888/',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(feedback),

        })
            .then((response) => response.text())
            .then(text => console.log(text));
    };

})();