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
        sendCommand("led on");
    };
    document.querySelector("#off").onclick = () => {
        sendCommand("led off");
    };

    document.querySelector("#flash").onclick = () => {
        let number = document.querySelector("#flashNum").value;
        let duration = document.querySelector("#duration").value;
        sendCommand(`flash ${number} ${duration}`);
    };  
}

main();