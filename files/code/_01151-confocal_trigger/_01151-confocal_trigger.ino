int Trig0 = 3;
int Trig1 = 2;
int FA = A1;
int NFA = A2;
bool NFAs = false;
bool triggered = false;
bool active =false;
int j = 0;

void setup() {
Serial.begin(9600);
while (!Serial) {
 ;//Waiting
}
//Serial.println("Start");
pinMode(Trig0, OUTPUT);
pinMode(Trig1, OUTPUT);
digitalWrite(Trig0, HIGH);
digitalWrite(Trig1, LOW);
}


String str = "";


void loop() {
  if (Serial.available()) {
    states(Serial.readStringUntil("\r\n"));
  }
  if (analogRead(FA) > 950 && !active && analogRead(NFA) < 50) {
    Serial.println("FA");
    active = true;
  } else if (analogRead(NFA) > 950 && active && analogRead(FA) < 50) {
    j = j + 1;
    Serial.println("FNA");
    //Serial.println(j);
    active = false;
  }

}

void states(String i) {
  i = i.toInt();
  if (i == "0") {
      digitalWrite(Trig0, HIGH);
      digitalWrite(Trig1, LOW);
      delay(50);
      digitalWrite(Trig0, LOW);
      digitalWrite(Trig1, HIGH);
      //Serial.println("Trigger");
  } else if (i == "1") {
      digitalWrite(Trig0, HIGH);
      digitalWrite(Trig1, LOW);
      Serial.println("HL");
  } else if (i == "2") {
      digitalWrite(Trig0, LOW);
      digitalWrite(Trig1, HIGH);
      Serial.println("LH");
  } else if (i == "3") {
      if (analogRead(FA) > 950 && analogRead(NFA) < 50) {
        Serial.println("FA");
        active = true;
      } else if (analogRead(NFA) > 950 && analogRead(FA) < 50) {
        j = j + 1;
        Serial.println("FNA");
        //Serial.println(j);
        active = false;
    }
  } else if (i == "4") {
    for (int k = 0; k < 10; k++) {
      triggered = false;
      while (!triggered) {
        digitalWrite(Trig0, HIGH);
        delay(500);
        digitalWrite(Trig0, LOW);
        delay(500);
        triggered = analogRead(FA) > 950 && analogRead(NFA) < 50;
      }
      Serial.print("Start:");
      Serial.print(k);
      for (int m = 0; m < 10; m++) { //TEST FOR ACTIVENESS
        if (analogRead(FA) > 950 && analogRead(NFA) < 50) {
          m = 0;
          delay(20);
        }
      }
      Serial.println(" DONE");
      delay(2000);
    }
  }
}


