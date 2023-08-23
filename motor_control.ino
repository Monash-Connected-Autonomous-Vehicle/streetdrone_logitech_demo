#include <Servo.h>
Servo L;
Servo R;

int incomingByte = 0;   // for incoming serial data

void setup() {
  Serial.begin(115200);
    L.attach(5);
  L.writeMicroseconds(1500);  // set servo to mid-point
   R.attach(6);
  R.writeMicroseconds(1500);  // set servo to mid-point
}

void loop() {

  // send data only when you receive data:
  char chararray[20];
  int pos = 0;
  while (Serial.available() > 0) {
    // read the incoming byte:
    char incomingByte = Serial.read();
    chararray[pos] = incomingByte;
    pos++;
    // say what you got:

    //Serial.println(incomingByte);
    Serial.println(chararray);
    //Serial.println(pos);
  }
  if (pos >= 3){
Serial.print(“I received: “);
  String pre_pwm = chararray;
  pre_pwm.remove(pos,20);
  long pwm = pre_pwm.toFloat();
  Serial.println(pwm);
  L.writeMicroseconds(pwm);
  R.writeMicroseconds(pwm);
  }
}
