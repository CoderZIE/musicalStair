#include <IRremote.h>

#define PIN_IR 10 
#define PIN_DETECT 12
#define PIN_IR2 9 
#define PIN_DETECT2 11 
#define PIN_IR3 9 
#define PIN_DETECT3 10
#define PIN_IR4 5 
#define PIN_DETECT4 9 

IRsend irsend;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_DETECT, INPUT);
  pinMode(PIN_DETECT2, INPUT); 
  pinMode(PIN_DETECT3, INPUT);
  pinMode(PIN_DETECT4, INPUT);
//  pinMode(PIN_IR, OUTPUT);
//  pinMode(PIN_IR2, OUTPUT);
//  pinMode(PIN_IR3, OUTPUT);
//  pinMode(PIN_IR4, OUTPUT);
//  digitalWrite(PIN_IR, HIGH);
//  digitalWrite(PIN_IR2, HIGH);
//  digitalWrite(PIN_IR3, HIGH);
//  digitalWrite(PIN_IR4, HIGH);
  irsend.enableIROut(38);
  irsend.mark(0);
}

void loop() {
if (digitalRead(PIN_DETECT) == LOW) {
    Serial.print("1");
} 
else if (digitalRead(PIN_DETECT2) == LOW) {
    Serial.print("2");
} 
else if (digitalRead(PIN_DETECT3) == LOW) {
    Serial.print("3");
} 
else if (digitalRead(PIN_DETECT4) == LOW) {
    Serial.print("4");
}
  Serial.println("");
  delay(100);
}
