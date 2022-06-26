#include <Servo.h>
char getinput;
Servo myservo;

void setup() {
  myservo.attach(9);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  myservo.write(90);
  Serial.println("Helloworld");
}
int val;
void loop() {
  delay(1000);
  getinput = Serial.read();
  myservo.write(getinput);
  Serial.println(1000 + myservo.read());
}
