#include <Arduino.h>

// Na Arduino Leonardo LED_BUILTIN (Pin 13) obsługuje PWM (analogWrite)
const int ledPin = LED_BUILTIN; 

void setup() {
  pinMode(ledPin, OUTPUT);
  analogWrite(ledPin, 0); // Startujemy od zera
  
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\r');
    command.trim(); 
    
    if (command == "START") {
      analogWrite(ledPin, 255); // Pełna jasność
      Serial.print("DONE\r");
    } 
    else if (command == "STOP") {
      analogWrite(ledPin, 0);   // Wyłączona
      Serial.print("DONE\r");
    }
    // Nowa logika: jeśli komenda zaczyna się od "SET:"
    else if (command.startsWith("SET:")) {
      // Wycinamy samą liczbę po dwukropku
      int brightnessPercent = command.substring(4).toInt(); 
      
      // Ograniczamy wartość do zakresu 0-100
      brightnessPercent = constrain(brightnessPercent, 0, 100);
      
      // Mapujemy 0-100% na zakres 0-255 dla analogWrite
      int pwmValue = map(brightnessPercent, 0, 100, 0, 255);
      
      analogWrite(ledPin, pwmValue);
      
      Serial.print("DONE\r");
    }
  }
}