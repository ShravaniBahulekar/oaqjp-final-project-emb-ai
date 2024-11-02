let RunSentimentAnalysis = () => {
    // Get the input text from the input field
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    // Create a new XMLHttpRequest
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        // Check if the request is complete
        if (this.readyState == 4) {
            // Check if the request was successful
            if (this.status == 200) {
                // Update the HTML with the server response
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                // Handle error responses
                document.getElementById("system_response").innerHTML = "Error: " + this.statusText;
            }
        }
    };

    // Open a POST request
    xhttp.open("POST", "/emotionDetector", true);
    // Set the request header to indicate JSON content
    xhttp.setRequestHeader("Content-Type", "application/json");
    
    // Send the request with the input text as a JSON string
    xhttp.send(JSON.stringify({ text: textToAnalyze }));
};
