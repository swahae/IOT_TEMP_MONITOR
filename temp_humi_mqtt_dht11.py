import paho.mqtt.client as mqtt
import Adafruit_DHT
import time
import json

# MQTT Credentials (change these)
USERNAME = "swathi"
PASSWORD = "Minjae19"
BROKER_URL = "2d661e1e01dd4910b6c995e2b90c1b5c.s1.eu.hivemq.cloud"  # Your HiveMQ hostname
PORT = 8883  # SSL Port

# DHT11 Config
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO4 (Pin 7 on Raspberry Pi)

# MQTT Callback


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to HiveMQ Cloud")
    else:
        print("❌ Connection failed, code:", rc)


# MQTT Client config
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()  # Enable SSL/TLS encryption
client.on_connect = on_connect

print("🔌 Connecting to MQTT Broker...")
client.connect(BROKER_URL, PORT, 60)
client.loop_start()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        data = {
            "temperature": temperature,
            "humidity": humidity
        }

        print(f"📡 Sending Data → Temp: {temperature}°C, Humidity: {humidity}%")

        client.publish("factory/data", json.dumps(data))
    else:
        print("⚠ DHT Sensor read failed — check wiring!")

    time.sleep(5)
