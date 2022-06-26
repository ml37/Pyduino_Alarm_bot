int data;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (data == '1') {
   digitalWrite (13, HIGH);
   delay(100);
   Serial.print(data);
  }
  else if (data == '0') {
  digitalWrite (13, LOW);
  delay(100);
  Serial.print(data);
  }
}
