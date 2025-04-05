function response = sendCommand(command)

apiUrl = "http://goikwj-tank.rose-hulman.edu:5000/api/";
getUrl = apiUrl + command;
response = webread(getUrl);

end