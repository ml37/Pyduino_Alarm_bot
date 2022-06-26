char getinput;

void setup() {
  pinMode(13, OUTPUT);
  // 시리얼 통신 시작 (boadrate: 9600)
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    getinput = Serial.read();
    if (getinput == '1') {
      digitalWrite(13, HIGH);
    } else if (getinput == '0') {
      digitalWrite(13, LOW);
    }

  }
}
