#include <WiFi.h>

bool activacion_canal = false;
const char* ssid = "IZZI-4542";
const char* password = "MGGAJI123mggaji- ";

WiFiServer server(12345);
WiFiClient cliente;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  //Configuramos WiFi
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("Conectandose....");
  }
  Serial.println("Cliente conectado");
  Serial.println(WiFi.localIP());

  //Preparamos el servidor
  server.begin();
}

void loop() {

  int valor = random(0,255);
  if(!cliente || !cliente.connected()){
    cliente = server.available();
  }

  cliente.println(valor);
  delay(1000);
  
}