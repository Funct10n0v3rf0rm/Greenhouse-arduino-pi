
#include "DHT.h"

#define DHTPIN 4     // what digital pin we're connected to
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
int photocellPin = 0;     // the cell and 10K pulldown are connected to a0
int photocellReading;     // the analog reading from the sensor divider       //
int ledPin =  2;      // the number of the LED pin
int ledState = LOW;             // ledState used to set the LED
unsigned long previousMillis = 0;        // will store last time LED was updated
unsigned long OnTime =  43200000;           // milliseconds of on-time
unsigned long OffTime = 43200000; // milliseconds of off-time
unsigned long increment = 320000;
unsigned long decrement = 1000;
int counter = 0;
//57600000 16 hours
//43200000 12 hours
//28800000 8 hours
//320000 5.3 minutes for adjustments
void setup() 
{
  // set the digital pin as output:
  pinMode(ledPin, OUTPUT);     
  Serial.begin(9600); 
  dht.begin();
}
 
void loop()
{
  // check to see if it's time to change the state of the LED
  unsigned long currentMillis = millis();
  
 if (currentMillis - previousMillis == 3600000) {
    photocellReading = analogRead(photocellPin);  
 
  Serial.print("Analog reading = ");
  Serial.println(photocellReading); // the raw analog reading
  if (photocellReading > 400) {
    Serial.println("light is on");
  }
  if (photocellReading < 400) {
    Serial.println("light is off");
  }
 
  // LED gets brighter the darker it is at the sensor
  // that means we have to -invert- the reading from 0-1023 back to 1023-0
  photocellReading = 1023 - photocellReading;
  //now we have to map 0-1023 to 0-255 since thats the range analogWrite uses
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);
  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print(f);
  Serial.print(" *F\t");
  Serial.print("Heat index: ");
  Serial.print(hic);
  Serial.print(" *C ");
  Serial.print(hif);
  Serial.println(" *F");
  
}
  if((ledState == HIGH) && (currentMillis - previousMillis >= OffTime))
  {
    ledState = LOW;  // Turn it on
    counter ++;
    if (counter < 45) {
    OnTime = OnTime + increment;
    OffTime = OffTime - increment;
    
  }
    else if (counter < 90) {
      OnTime = OnTime - increment;
      OffTime = OffTime + increment;
    }
   if (counter > 90) {
    counter = 0;
   }
    
    previousMillis = currentMillis;  // Remember the time
    digitalWrite(ledPin, ledState);  // Update the actual LED
    Serial.print("currentMillis:");
    Serial.println(currentMillis);
    Serial.print("previousMillis:");
    Serial.println(previousMillis);
    Serial.print("OnTime:");
    Serial.println(OnTime);
    Serial.print("OffTime:");
    Serial.println(OffTime);
    Serial.print("Counter:");
    Serial.println(counter);
    
  }
  else if ((ledState == LOW) && (currentMillis - previousMillis >= OnTime))
  {
    
    ledState = HIGH;  // turn it off
    previousMillis = currentMillis;   // Remember the time
    digitalWrite(ledPin, ledState);	  // Update the actual LED
    Serial.print("currentMillis:");
    Serial.println(currentMillis);
    Serial.print("previousMillis:");
    Serial.println(previousMillis);
    Serial.print("OnTime:");
    Serial.println(OnTime);
    Serial.print("OffTime:");
    Serial.println(OffTime);
  }
}

