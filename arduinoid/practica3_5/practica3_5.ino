// Instalar la libreria Arduinojson by benoit 
#include<ArduinoJson.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  StaticJsonDocument<200> doc;

  JsonArray labels = doc.createNestedArray("labels");
  labels.add("A");
  labels.add("B");
  labels.add("C");
  labels.add("D");

  JsonArray values = doc.createNestedArray("values");
  values.add(random(20,100));
  values.add(random(20,100));
  values.add(random(20,100));
  values.add(random(20,100));

  serializeJson(doc,Serial);
  Serial.println();
  delay(1000);
}
