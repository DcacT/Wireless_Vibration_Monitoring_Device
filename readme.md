# Wireless_Vibration_Monitoring_Device

## Introduction
Wireless_Vibration_Monitoring_Device is a prototype designed to monitor vibrations wirelessly using an Arduino Uno, accelerometer, and BLE 4.0 technology. By utilizing Bluetooth Low Energy (BLE) communication, the device sends vibration data to a host device for further analysis.

This is a final project of McMaster Automation Engineering 4MH3 course. This prototype serves as an initial step toward creating cost-effective, portable, and scalable wireless vibration monitoring solutions for industrial application. 

The purpose of this upload is to set as a case example for arduino to BLE connection. 

## Features
- Real-time vibration monitoring using an accelerometer.
- Wireless communication enabled by BLE 4.0.
- Uses the `ble_serial` library to facilitate seamless communication between the Arduino Uno and the HM-10 BLE module.
- Portable and lightweight design for easy deployment.

## Components
- **Arduino Uno**: The microcontroller board used to control the accelerometer and BLE module.
- **HM-10 BLE Module**: A Bluetooth Low Energy module that enables wireless communication.
- **Accelerometer ADXL335**: A sensor that measures acceleration in three axes (X, Y, Z).
- **ble_serial Library**: A library used to simplify the Arduino-to-HM-10 connection.

## Software 
- **bt_reciever.py**:Handles bluetooth connection & infromation recieved from arduino. Can enable tcp to forward information to tcp addresses for industrial application, which in this case is just a data visualizer. 
- **visualizer.py**:Sets up a tcp server listening for formatted data from bt_reciever.py. Right now it just plot the data out in real time for visualization. 
- **report_generation.py**:Generate report of frequency analysis with FFT. 
- **4MH3_CourseProj_bluetooth_module.ino**:Handles arduino things, assign pins as per table below, and send formatted sensor data to recieving device.   

## Hardware Connections

| Component         | Pin      | Arduino           |
|-------------------|----------|-------------------|
| Accelerometer     | Vcc      | 5V                |
|                   | X        | A0                |
|                   | Y        | A1                |
|                   | Z        | A2                |
| Bluetooth (HM-10) | Vcc      | 5V                |
|                   | Tx       | Digital2 Rx       |
|                   | Rx       | Digital3 Tx       |
|                   | Gnd      | GND               |
| PSU               | Vin      | Power Supply      |
|                   | Gnd      | GND               |

   

## Report 
A project [report](report\4MH3_Project_Report.docx) is included in the repository for further expanation. 

## Notes
Huge thanks to Amos Liang and ChatGPT.  


