int pumpPin1 = 3;
int pumpPin2 = 2;
int pumpState1 = LOW;
int pumpState2 = LOW;
unsigned long OnTime1 = 90000;
unsigned long OffTime1 = 259200000;
unsigned long OnTime2 = 90000;
unsigned long OffTime2 = 259800000;
unsigned long previousMillis = 0;
unsigned long previousMillis2 = 0;
//259200000 - three days in ms
// 600000   - ten minutes in ms
// there's currently a ten minute gap, but this will cause the pumps to drift ten minutes per day
// I need a to make so that pump one runs for 90 seconds, twenty minute gap, then pump two runs. 
// the arduino clock drifts a little each day, but that's ok for now, future upgrade to use a raspberry pi clock
// the goal is to run two arduinos as slaves to one raspberry pi in the long run.

void setup() {
  // put your setup code here, to run once:
   // set the digital pin as output:
  pinMode(pumpPin1, OUTPUT);
  pinMode(pumpPin2, OUTPUT);     
  Serial.begin(9600); 

}

void loop()
{
  // check to see if it's time to change the state of the Pump
  unsigned long currentMillis = millis();
  unsigned long actualMillis = millis();
  unsigned long currentMillis2 = millis();

  
  
 
    if((pumpState1 == HIGH) && (currentMillis - previousMillis >= OffTime1))
  {
    pumpState1 = LOW;  // Turn it on
    Serial.print("pump1 is on: ");
    Serial.print("currentMillis:");
    Serial.println(currentMillis);
    Serial.print("previousMillis:");
    Serial.println(previousMillis);
    Serial.print("actualMillis:");
    Serial.println(actualMillis);
    previousMillis = currentMillis;
    digitalWrite(pumpPin1, pumpState1);
    
  }
    else if ((pumpState1 == LOW) && (currentMillis - previousMillis >= OnTime1))
  {
    pumpState1 = HIGH;  // turn it off
    Serial.print("pump1 is off: ");
    Serial.print("currentMillis:");
    Serial.println(currentMillis);
    Serial.print("previousMillis:");
    Serial.println(previousMillis);
    Serial.print("actualMillis:");
    Serial.println(actualMillis);
    previousMillis = currentMillis;
    digitalWrite(pumpPin1, pumpState1);
  }
   if((pumpState2 == HIGH) && (currentMillis2 - previousMillis2 >= OffTime2))
  {
    pumpState2 = LOW;  // Turn it on
    Serial.print("pump2 is on: ");
    Serial.print("currentMillis2:");
    Serial.println(currentMillis2);
    Serial.print("previousMillis2:");
    Serial.println(previousMillis2);
    Serial.print("actualMillis:");
    Serial.println(actualMillis);
    previousMillis2 = currentMillis2;
    digitalWrite(pumpPin2, pumpState2);
  }
    else if ((pumpState2 == LOW) && (currentMillis2 - previousMillis2 >= OnTime2))
  {
    
    pumpState2 = HIGH;  // turn it off
    Serial.print("pump2 is off: ");
    Serial.print("currentMillis2:");
    Serial.println(currentMillis2);
    Serial.print("previousMillis2:");
    Serial.println(previousMillis2);
    Serial.print("actualMillis:");
    Serial.println(actualMillis);
    previousMillis2 = currentMillis2;
    digitalWrite(pumpPin2, pumpState2);
  }
}
  
