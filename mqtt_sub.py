import time
from tkinter import N
import paho.mqtt.client as paho
import json

broker="10.20.1.95"
def on_message(client, userdata, message):
    time.sleep(1)
    #print("received message =",str(message.payload.decode("utf-8")))
    F = json.loads(str(message.payload.decode()))
    print("Name: ", F["name"])
    print("surname: ", F["surname"])
    print("telephone: ", F["telephone"])
    print("grade: ", F["grade"])

client= paho.Client()
client.on_message=on_message
print("connecting to broker ",broker)
client.connect(broker)
client.loop_start() 
print("subscribing ")
client.subscribe("alfaisal/Faisal-200271")
while(True):
	client.on_message=on_message
