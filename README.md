# 🌡️ Industrial Temperature & Distance IoT Monitor

An IoT-based monitoring system using Raspberry Pi Zero 2W that measures temperature and humidity, displays the values on an LCD, and publishes sensor data to an MQTT broker for real-time monitoring using Node-RED.

---

## 📌 Project Overview

This project collects environmental temperature data using sensors connected to a Raspberry Pi and sends the data to a cloud MQTT broker (HiveMQ Cloud). The data can then be visualized in Node-RED dashboards.

### Features

- Temperature monitoring using DHT11
- Humidity monitoring using DHT11
- Distance measurement using HC-SR04 Ultrasonic Sensor
- Real-time display on 16x2 I2C LCD
- MQTT communication via HiveMQ Cloud
- Node-RED dashboard integration
- Real-time monitoring and visualization

---
## Flow

<img width="1280" height="618" alt="image" src="https://github.com/user-attachments/assets/fa09f231-33d9-47a9-891c-36eccf99e9c8" />

---
## 🛠 Hardware Components

| Component | Quantity |
|------------|----------|
| Raspberry Pi Zero 2W | 1 |
| DHT11 Sensor | 1 |
| 16x2 LCD with I2C Module | 1 |
| Breadboard | 1 |
| Jumper Wires | As Required |

---

## 🔌 Circuit Connections

### DHT11

| DHT11 | Raspberry Pi |
|--------|-------------|
| VCC | 3.3V |
| DATA | GPIO4 |
| GND | GND |

### I2C LCD

| LCD | Raspberry Pi |
|------|-------------|
| VCC | 5V |
| GND | GND |
| SDA | GPIO2 (SDA) |
| SCL | GPIO3 (SCL) |

---
## Setup

<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/11fc676e-b988-4f71-b58e-062b193d9e5b" />

---
## ⚙️ Software Requirements

### Raspberry Pi

Update packages:

```bash
sudo apt update
sudo apt upgrade -y
```

Install required libraries:

```bash
pip3 install paho-mqtt
pip3 install Adafruit_DHT
pip3 install RPLCD
pip3 install smbus2
```

Install MQTT client tools:

```bash
sudo apt install mosquitto-clients -y
```

---

## ☁️ HiveMQ Cloud Setup

1. Create a HiveMQ Cloud account.
2. Create a new cluster.
3. Create MQTT credentials.
4. Note the following:

```text
Broker URL
Username
Password
Port: 8883
```

Example:

```text
Broker:
your-cluster.s1.eu.hivemq.cloud

Topic:
factory/data
```
<img width="1280" height="679" alt="image" src="https://github.com/user-attachments/assets/594bc4a4-fdfc-4144-94a3-94a3a7886f58" />

---

## 📡 MQTT Data Format

Published Topic:

```text
factory/data
```

Sample Payload:

```json
{
  "temperature": 28,
  "humidity": 65
}
```

---

## 📊 Node-RED Flow

Required Nodes:

- MQTT IN
- JSON
- Debug

Flow:

```text
MQTT IN → JSON → Debug
```

MQTT Configuration:

| Parameter | Value |
|------------|--------|
| Server | HiveMQ Broker URL |
| Port | 8883 |
| TLS | Enabled |
| Topic | factory/data |

<img width="1280" height="644" alt="image" src="https://github.com/user-attachments/assets/23a4e455-4f8e-4956-bec4-044db3a5244e" />

---

## 🚀 Running the Project

Run the Python script:

```bash
python3 monitor.py
```

Expected Output:

```text
Connected to HiveMQ Cloud
Temperature: 28°C
Humidity: 65%
Published Successfully
```
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/23eaaaca-b13f-462d-bd9b-f87647e26f10" />

---

## 📁 Project Structure

```text
Industrial-Temperature-Monitor/
│
├── monitor.py
├── README.md
├── requirements.txt
└── images/
    ├── circuit_diagram.png
    ├── lcd_output.jpg
    └── node_red_dashboard.png
```

---

Industrial Temperature IoT Monitor using Raspberry Pi, MQTT, HiveMQ Cloud, and Node-RED.
