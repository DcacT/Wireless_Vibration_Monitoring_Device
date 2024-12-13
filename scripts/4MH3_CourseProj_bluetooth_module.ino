#include <SoftwareSerial.h>
SoftwareSerial HM10(2, 3); // RX = 2, TX = 3
String HM10_read;
void setup() {
  // Start serial communication at 9600 baud for Serial Monitor and Bluetooth
  Serial.begin(9600);
  HM10.begin(9600); // set HM10 serial at 9600 baud rate

  Serial.println("Hello, HM-10 Bluetooth!");
}

void loop() {
  // You can use Serial.println() to send data to the Bluetooth module
  HM10.listen();  // listen the HM10 port
  while (HM10.available() > 0) {   // if HM10 sends something then read

    HM10_read = String(HM10.read());
    Serial.write("r");
  }

  if(1){
    int x = analogRead(A0);
    int y = analogRead(A1);
    int z = analogRead(A2);
    
    // Create a formatted string to send to Bluetooth
    String dataToSend = "(" + String(x) + "," + String(y) + "," + String(z) + ")";
    
    // Convert string to byte array
    byte dataBytes[dataToSend.length() + 1];  // +1 for the null terminator
    dataToSend.getBytes(dataBytes, dataToSend.length() + 1);  // Include null terminator
    
    // Debug: print the string you're trying to send
    Serial.print("Sending data: ");
    Serial.println(dataToSend);
    
    HM10.write(dataBytes, dataToSend.length() + 1);  // Send the exact number of bytes
  }
  delay(1);  // Delay for ms
}
