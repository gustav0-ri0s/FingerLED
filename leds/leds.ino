int leds[] = {2, 3, 4, 5, 6}; // Pines para los 5 LEDs

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }
}

void loop() {
  if (Serial.available()) {
    int dedos = Serial.parseInt();
    for (int i = 0; i < 5; i++) {
      if (i < dedos) {
        digitalWrite(leds[i], HIGH);
      } else {
        digitalWrite(leds[i], LOW);
      }
    }
  }
}
