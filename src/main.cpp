#include <Arduino.h>

#ifndef yaml_params
#define param_la_kp 4
#endif

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(param_la_kp);
}