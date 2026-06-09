function sendMessage() {
    let msg = document.getElementById("userInput").value;
    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("chat").innerHTML +=
        "<p><b>You:</b> " + msg + "</p>" +
        "<p><b>Bot:</b> " + data.response + "</p>";
    });
}