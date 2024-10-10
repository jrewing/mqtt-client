import paho.mqtt.client as mqtt

# Define the MQTT client
client = mqtt.Client()

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("broker.hivemq.com", 1883, 60)

# Start the loop to process received messages
client.loop_forever()