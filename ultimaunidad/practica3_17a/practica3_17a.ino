#include<WiFi.h>
#include<HTTPClient.h>

const char* ssid = "IZZI-4542";
const char*  password="MGGAJI123mggaji- ";
//const char* ssid = "informatica7";
//const char* password = "Info_@@7";
//WiFiServer serve(12345);

//WiFiClient cliente;

void setup() {
 Serial.begin(115200);
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("Conectandose....");
  }
  Serial.println(WiFi.localIP());
  Serial.println(WiFi.status());
  /*if(cliente.connect(ip,puerto)){
    Serial.println("Si se conecto al servidor");
  }else{
    Serial.println("No se conecto...");
  }*/
}
void loop() {
  if(WiFi.status() == WL_CONNECTED){
     HTTPClient cliente;
    cliente.begin("http://192.168.1.15:8000/api/sensores");//la ip de tu computadora
    cliente.addHeader("Content-Type","application/json");
    int valor = random(0,70);
    String json = "{\"valor\":" + String(valor) + "}";
    int respuesta = cliente.POST(json);
    if(respuesta>0){
      Serial.println(cliente.getString());
    }else{
      Serial.print("Error: ");
      Serial.println(respuesta);
    }
    cliente.end();
  }
  delay(1000);
}


/*
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "IZZI-4542";
const char* password = "MGGAJI123mggaji- ";

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectándose...");
  }

  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient cliente;

    cliente.begin("http://192.168.1.15:8000/api/sensores");
    cliente.addHeader("Content-Type", "application/json");

    int sensor1 = random(0, 70);
    int sensor2 = random(100, 200); // ejemplo de segundo dato

    //JSON con 2 datos
    String json = "{\"sensor1\":" + String(sensor1) +
                  ",\"sensor2\":" + String(sensor2) + "}";

    int respuesta = cliente.POST(json);

    if (respuesta > 0) {
      Serial.println(cliente.getString());
    } else {
      Serial.print("Error: ");
      Serial.println(respuesta);
    }

    cliente.end();
  }

  delay(1000);
}

*/