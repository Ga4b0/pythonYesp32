
#define trig 25
#define echo 33

float distancia;
//BluetoothSerial conexion;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);

  Serial.println("Hola desde la esp32");
  
}

void loop() {

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
  Serial.print("distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");

  //conexion.write(distancia);
  delay(500);
}