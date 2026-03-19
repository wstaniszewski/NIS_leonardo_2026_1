#include <Arduino.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW); 
  
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available() > 0) {
    // ZMIANA 1: Nasłuchujemy do znaku CR ('\r'), który wyśle NIS
    String command = Serial.readStringUntil('\r');
    command.trim(); 
    
    if (command == "START") {
      digitalWrite(LED_BUILTIN, HIGH);
      
      // ZMIANA 2: Używamy print zamiast println i ręcznie dodajemy znak CR ('\r') na końcu
      Serial.print("DONE\r"); 
    } 
    else if (command == "STOP") {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.print("DONE\r");
    }
  }
}