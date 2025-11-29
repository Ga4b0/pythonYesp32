#include<ArduinoJson.h>
#include<WiFi.h>

//const char* ssid = "informatica7";
//const char* password = "Info_@@7";
const char* ssid = "IZZI-4542";
const char*  password="MGGAJI123mggaji- ";
//WiFiServer server(12345);
const char* ip = "192.168.1.15"; // la esp usa la ip para conectarse
const int puerto = 5001; // puerto; 
WiFiClient cliente;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("conectandose...");
  }
  if(cliente.connect(ip,puerto)){
    Serial.println("si se conecto al servidor");

  }else {
    Serial.println("no se conecto....");
  }
}

void loop() {
  int g = random(1,255);
  StaticJsonDocument<100> doc;
  JsonArray labels = doc.createNestedArray("labels");
  labels.add("valor");
  JsonArray values = doc.createNestedArray("values");
  values.add(g);
  String datos;
  serializeJson(doc,datos);

  if(cliente.connected()){
    cliente.println(datos);
  }else{
    if(cliente.connect(ip,puerto)){
    Serial.println("El cliente se conecto");
    }
  }

  
  delay(1000);
  
}
