import paho.mqtt.client as mqtt
import logging
logging.basicConfig(level=logging.DEBUG)

def on_log(client, userdata, level, buf):
    print(f"Log: {buf}")

# Define the MQTT client
client = mqtt.Client()
client.tls_set(ca_certs=None, 
               certfile="secrets/manta-api-serverclient.pem", 
               keyfile="secrets/manta_serverclient_private.key")
client.username_pw_set("manta-test-serverclient", None)  # Set the username here
client.on_log = on_log
# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("egns-data-processing-test-01.westeurope-1.ts.eventgrid.azure.net", 8883, 60)

# Start the loop to process received messages
client.loop_forever()