int IRSensor = 2;
int LED = 13;
int value;
int led2 = 8;

int data;
int verificare = 8;
int numar;
int contor = 0;



void setup()
{
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}


void loop()
{
  while(contor < 8) {
  value = digitalRead(IRSensor);
  Serial.println(value);
  contor = contor + 1;
  delay(5000);
  }

  while (Serial.available())
  {
    numar = Serial.read();
  }

  if (numar == '1') {
    digitalWrite(led2, HIGH);
  }
  else if (numar == '0') {
    digitalWrite(LED, HIGH);
  }
  
  delay(5000);

}
