function checkSpam() {
    let text = document.getElementById("textInput").value;

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {
        let box = document.getElementById("resultBox");

        box.innerHTML =
            "Score: " + data.score + "<br>" +
            "Matched Words: " + data.matched.join(", ") + "<br>" +
            "Result: " + data.result;

        box.style.color = data.result === "SPAM" ? "red" : "green";
    });
}