#define ECHO 36
#define TRIG 37
#define LED_PIN 42
#define SWITCH_PIN 52

void trigger();
float measureDistance();

// Speed of sound in cm/us
const float sound_speed = 0.034;

void setup() {

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  pinMode(LED_PIN, OUTPUT);
  pinMode(SWITCH_PIN, INPUT);

  Serial.begin(9600);

}

void loop() {

  int switch_status = digitalRead(SWITCH_PIN);
  digitalWrite(LED_PIN, !switch_status);

  if (switch_status == LOW) {
    Serial.println("switch ON");
  }

  trigger();
  float distance = measureDistance();
  
  Serial.print("distance ");
  Serial.println(distance);

  delay(100);

}

void trigger() {
  
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  
}

float measureDistance() {

  long duration = pulseIn(ECHO, HIGH);
  return (duration * sound_speed) / 2;

}
