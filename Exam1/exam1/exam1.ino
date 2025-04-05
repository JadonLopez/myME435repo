String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(19200);
  inputString.reserve(200);
  pinMode(13,OUTPUT);
}

void loop() {
  if (stringComplete) {
    if (inputString.equals("led on")) {
    digitalWrite(13,1);
    } else if (inputString.equals("led off")) {
      digitalWrite(13,0);
    } else if (inputString.startsWith("flash")) {
      String params = inputString.substring(6);
      int spaceIndex = params.indexOf(' ');
      if (spaceIndex > 0) {
        String numberStr = params.substring(0, spaceIndex);
        String durationStr = params.substring(spaceIndex + 1);

        int number = numberStr.toInt();
        int duration = durationStr.toInt();
        for (int i = 0; i < number; i++) {
          digitalWrite(13,0);
          delay(duration/2);
          digitalWrite(13,1);
          delay(duration/2);
          digitalWrite(13,0);
        }
      }
    } else {
      Serial.print("Unknown command --> ");
      Serial.println(inputString);
    }
    inputString = "";
    stringComplete = false;
    Serial.println("Done!");
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}