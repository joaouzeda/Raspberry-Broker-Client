from application.configs.broker_configs import mqtt_broker_configs

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT Broker! Client: {client}")
        client.subscribe(mqtt_broker_configs.TOPIC)
    else:
        print(f"Failed to connect, return code = {rc}")

def on_subscribed(client, userdata, mid, granted_qos):
    print(f"Client Subscribed at {mqtt_broker_configs["TOPIC"]}")
    print(f"Qos: {granted_qos}")

def on_message(client, userdata, message):
    print("Recived message")
    print(client)
    print(message.payload)