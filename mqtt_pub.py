import paho.mqtt.client as mqtt
import json

# broker_address="localhost"
broker_address="10.20.1.95"
client = mqtt.Client()
topic = "alfaisal/Faisal-200271"
x = {
  "name": "Faisal",
  "surname": "almadi",
  "telephone": 111111111,
  "grade":100
}
y = json.dumps(x)
message = y
if (client.connect(broker_address,1883,60) ==0):
	print ("Connected succesfully to "+broker_address)
	print ("Published in "+topic+", msg = "+message)
client.publish(topic, message)
client.disconnect();