int ledPin = 13;  // Pin where the LED is connected

void setup() {
  pinMode(ledPin, OUTPUT);  // Set pin 13 as an output
  Serial.begin(9600);       // Start serial communication at 9600 baud rate
}

void loop() {
  digitalWrite(ledPin, HIGH);  // Turn the LED on
  delay(2000);  // Wait for 500 milliseconds (0.5 seconds)
  
  digitalWrite(ledPin, LOW);   // Turn the LED off
  delay(2000);  // Wait for 500 milliseconds (0.5 seconds)
  /*if (Serial.available() > 0) {
    char command = Serial.read();  // Read the incoming byte

    if (command == '1') {          // If command is '1', turn the LED on
      digitalWrite(ledPin, HIGH);
    } 
    else if (command == '0') {     // If command is '0', turn the LED off
      digitalWrite(ledPin, LOW);
    }
  }*/
}
