import paho.mqtt.client as mqtt
import time
import random

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("Parking/")

def on_message(client, userdata, msg):
    print(f"Сообщение от броккера! {msg.topic}: {str(msg.payload)}")

client = mqtt.Client(client_id="123", clean_session=True, userdata=None, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883)

client.loop_start()
while True:
    test_object = {"id": random.randint(1, 30), "occupied": random.choice((True, False))}
    client.publish("Parking/", str(test_object))
    time.sleep(30)
