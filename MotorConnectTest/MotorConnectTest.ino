#include <Servo.h>
char getinput;
Servo myservo;

void setup() {
  myservo.attach(9);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  myservo.write(90);
}
int val;
void loop() {
  getinput = Serial.read();
  if (getinput =='a') {
    myservo.write(0);
  }
  if (getinput =='b') {
    myservo.write(90);
  }
  if (getinput == 'c') {
    myservo.write(180);
  }
}
