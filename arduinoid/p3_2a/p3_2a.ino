#include "BluetoothSerial.h"

#define trig 25
#define echo 33

//Variable para guardar distancia
float distancia;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  //Preparamos el TRIG: lo apagamos brevemente
  digitalWrite(trig,LOW);
  delayMicroseconds(2);

  //Enviamos un pulso ultrasonico de 10 microsegundos
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);

  //Medimos el tiempo que tarda en regresar el eco (en microsegundos)
  distancia = pulseIn(echo,HIGH);

  //Convertimos ese tiempo a distnacia en centimetros
  //Formula: distancia (cm) = tiempo
  distancia = distancia/58;

  //Mostramos la distancia en el monitor serial
  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");

  delay(500);
}