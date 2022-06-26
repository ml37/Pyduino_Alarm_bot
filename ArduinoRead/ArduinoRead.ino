
int data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(12, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  data = digitalRead(12);
  Serial.println(data);
  delay(1000);
}
