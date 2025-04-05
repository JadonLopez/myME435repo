async function sendCommand(command) {
    let response = await fetch(`/api/${command}`);
    let responseText = await response.text();
    console.log(responseText);

    //Display this responseText to the screen.
    document.querySelector("#responseText").innerHTML = responseText;
}

function main() {
    console.log("Ready!");

    document.querySelector("#on").onclick = () => {
        sendCommand("LED On");
    };
    document.querySelector("#off").onclick = () => {
        sendCommand("LED Off");
    };

    document.querySelector("#flash").onclick = () => {
        let number = document.querySelector("#flashNum").value;
        let duration = document.querySelector("#duration").value;
        sendCommand(`Flash ${number} ${duration}`);
    };  
}

main();