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
  }
  else if (data == '0') {
  digitalWrite (13, LOW);
  }
}
