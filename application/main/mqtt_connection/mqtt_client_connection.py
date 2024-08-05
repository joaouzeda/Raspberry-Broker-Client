import paho.mqtt.client as mqtt

from application.main.mqtt_connection.callbacks import on_message, on_subscribed, on_connect

class MqttClientConnection:
    def __init__(self, broker_ip: str, port: int, client_name, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port 
        self.__client_name = client_name
        self.__keepalive = keepalive
        self.__mqtt_client = None
    def start_connection(self):
        mqtt_client = mqtt.Client(self.__client_name)
        
        #callbacks
        mqtt_client.on_connect = on_connect
        mqtt_client.on_subscribed = on_subscribed
        mqtt_client.on_message = on_message

        #publishers

        mqtt_client.connect(host= self.__broker_ip, port=self.__port, keepalive=self.__keepalive)
        self.__mqtt_client = mqtt_client
        self.__mqtt_client.loop_start()

    def end_connection(self):
        try:
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()
            return True
        except:
            return False