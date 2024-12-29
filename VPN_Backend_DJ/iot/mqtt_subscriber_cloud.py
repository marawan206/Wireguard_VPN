# this line related to django model
from .models import DeviceStatus

import paho.mqtt.client as mqtt
import json
import ssl
import os

# MQTT Broker settings
BROKER = "10.0.0.1"
PORT = 8883
STATUS_TOPIC = "iot/status"

# Paths to certificates
ca_path = os.path.join(os.path.dirname(__file__), "ca.crt")
cert_path = os.path.join(os.path.dirname(__file__), "client.crt")
key_path = os.path.join(os.path.dirname(__file__), "client.key")

# Callback for connection status
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker successfully.")
        # Automatically subscribe upon successful connection
        client.subscribe(STATUS_TOPIC)
        print(f"Subscribed to topic: {STATUS_TOPIC}")
    else:
        print(f"Failed to connect to broker. Return code: {rc}")

# Callback for message reception
def receive_message(client, userdata, message):
    try:
        print(f"Message received on topic: {message.topic}")
        payload = message.payload.decode()
        print(f"Payload: {payload}")
        
        # Parse JSON and log parsed data
        data = json.loads(payload)
        print(f"Parsed data: {data}")
        
        # Handle data, e.g., update the DeviceStatus model
        device = DeviceStatus.objects.first()
        if device:
            new_status = data.get("status", "UNKNOWN")
            device.status = new_status
            device.save()
            print(f"Device status updated to: {new_status}")
        else:
            print("No DeviceStatus instance found in the database.")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Function to start the MQTT client
def start_mqtt_client():
    try:
        print("Initializing MQTT client...")
        client = mqtt.Client()

        # Set TLS/SSL parameters
        client.tls_set(
            ca_certs=ca_path,
            certfile=cert_path,
            keyfile=key_path,
            cert_reqs=ssl.CERT_REQUIRED,
            tls_version=ssl.PROTOCOL_TLSv1_2
        )
        client.tls_insecure_set(True)

        # Set username and password
        client.username_pw_set("username", "password")

        # Assign callbacks
        client.on_connect = on_connect
        client.on_message = receive_message

        # Connect to the broker
        print("Connecting to broker...")
        client.connect(BROKER, PORT, 60)

        # Start the client loop
        client.loop_start()
        print("MQTT client is running and awaiting messages...")
    except FileNotFoundError as e:
        print(f"Certificate file not found: {e}")
    except Exception as e:
        print(f"Error initializing MQTT client: {e}")
