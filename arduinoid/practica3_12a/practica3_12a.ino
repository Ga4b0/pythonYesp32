#include <ArduinoJson.h>

bool ban = false;
void setup() {
  Serial.begin(115200);
}

void loop() {
  StaticJsonDocument<100> doc;
  if(ban){
    int valor1 = random(1,100);
    int valor2 = random(1,100);
    JsonArray labels = doc.createNestedArray("labels");
    labels.add("Valor1");
    labels.add("Valor2");

    JsonArray values = doc.createNestedArray("values");
    values.add(valor1);
    values.add(valor2);

    serializeJson(doc,Serial);
    Serial.println();

  }
  if (Serial.available()){
    char c = Serial.read();
    if (c == '1'){
      ban = !ban; 
    }
  }
  delay(250);
}
