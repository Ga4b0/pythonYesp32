#include "BluetoothSerial.h"
#include <ArduinoJson.h>

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth no está habilitado
#endif


BluetoothSerial puerto;

void setup() {
  Serial.begin(115200);
  puerto.begin("ESP_GaboL");  // Nombre Bluetooth del ESP32
}

void loop() {
  // Simulación de dos valores aleatorios para enviar como JSON
  int valor1 = random(1,100);
  puerto.println(valor1);
  Serial.println(valor1);

  delay(300);  // Envío cada 0.3 segundos
}
