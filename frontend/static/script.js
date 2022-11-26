"use strict";

// alert("hello");


// alert(document.getElementById("application_text").value);

(function () {
    let btn_submit = document.getElementById("btn_submit");
    btn_submit.onclick = function (event) {
        event.preventDefault();
        let feedback = {};
        feedback.sender = {};
        feedback.sender.last_name = document.getElementById("last_name").value;
        feedback.sender.first_name = document.getElementById("first_name").value;
        feedback.sender.patronym = document.getElementById("patronym").value;
        feedback.sender.phone = document.getElementById("phone").value;
        feedback.message = document.getElementById("feedback_text").value;
        console.log(JSON.stringify(feedback));
    };
})();