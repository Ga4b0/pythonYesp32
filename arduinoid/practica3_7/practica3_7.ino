// Instalar la libreria Arduinojson by benoit 
#include<ArduinoJson.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  StaticJsonDocument<100> doc;


  doc["labels"] = "Sensor";
  doc["values"] = random(10,200);
  /*
  JsonArray labels = doc.createNestedArray("labels");
  labels.add("");

  JsonArray values = doc.createNestedArray("values");
  values.add(random(20,100));*/

  serializeJson(doc,Serial);
  Serial.println();
  delay(1000);
}
