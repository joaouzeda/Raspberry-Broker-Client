import paho.mqtt.client as mqtt

mqtt_client = mqtt.Client('Raspbeery')
mqtt_client.connect(host = "localhost", port = 1883)
mqtt_client.publish(topic = "/messages", payload = '{"Minha mensagem" : "Teste"}')

print('end publish')