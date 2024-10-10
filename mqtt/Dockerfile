FROM python:3.9-slim

# Install necessary dependencies
RUN pip install paho-mqtt

# Copy the MQTT client code into the container
COPY . /app
WORKDIR /app

# Define the command to run the MQTT client
CMD ["python", "mqtt_client.py"]